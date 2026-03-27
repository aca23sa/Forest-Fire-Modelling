# Name: Wildfire Simulation
# Dimensions: 2

# --- Set up executable path, do not edit ---
import sys
import inspect
this_file_loc = (inspect.stack()[0][1])
main_dir_loc = this_file_loc[:this_file_loc.index('ca_descriptions')]
sys.path.append(main_dir_loc)
sys.path.append(main_dir_loc + 'capyle')
sys.path.append(main_dir_loc + 'capyle/ca')
sys.path.append(main_dir_loc + 'capyle/guicomponents')
# ---

from capyle.ca import Grid2D, Neighbourhood, CAConfig, randomise2d
import capyle.utils as utils
import numpy as np

# =============================
# Global variables
# =============================
water_zone_global = None        
water_drop_info = None            
step_count_global = 0             # Number of CA steps elapsed
town_burn_time_global = None      # When the town starts burning
town_positions_global = None      # Coordinates of town cells

# Simulation constants
HOURS_PER_STEP = 1.0              # Each CA step = 1 hour of simulated time
WATER_AREA_KM2 = 12.5             # Fixed area covered by a water drop
WIND_DIRECTION = 'S'              # Global wind direction 

# Burnt : 0, Burning : 1, Chapparal : 2, Lake : 3, Forest : 4, Canyon : 5, Town : 6, Water Drop : 9

# =============================
# Helper
# =============================
def draw(arr, start_x, end_x, start_y, end_y, terrain):
    for y in range(int(start_y*4), int(end_y*4)):
        for x in range(int(start_x*4), int(end_x*4)):
            arr[y, x] = terrain

# =============================
# Wind effect grid
# =============================
def wind_func(direction):

    base_wind = np.array([[1.0, 1.0, 1.0], [1.0, 0.0, 1.0], [1.0, 1.0, 1.0]]) # Default wind influence (no strong direction)

    dirs = {'N':  (0,1), 'NE': (0,2), 'E':  (1,2), 'SE': (2,2), 'S':  (2,1), 'SW': (2,0), 'W':  (1,0), 'NW': (0,0)} # Map directions to a 3×3

    opposite = {'N':'S','NE':'SW','E':'W','SE':'NW','S':'N','SW':'NE','W':'E','NW':'SE'}

    if direction not in dirs:
        return base_wind

    down_row, down_col = dirs[direction]
    base_wind[down_row, down_col] *= 3.0  # stronger downwind

    up_row, up_col = dirs[opposite[direction]]
    base_wind[up_row, up_col] *= 0.1  # weaker upwind

    return base_wind

# =============================
# Core CA transition
# =============================
def transition_func(grid, neighbourstates, neighbourcounts, burntgrid, ignition_grid, wind_direction=WIND_DIRECTION):
    """
    Main fire spread rules:
    - Burning cells burn out over time.
    - Unburnt neighbours can ignite depending on terrain, wind, and water.
    """
    burning_cells = (grid == 1) | (grid == 7)

    # Non-flammable terrain
    lake_cells = (grid == 3)
    water_cells = (grid == 9)
    non_flammable = lake_cells | water_cells

    # Unburnt flammable terrain (forest, canyon, chaparral)
    unburnt_cells = (grid >= 2) & ~non_flammable

    # Cells that have burning neighbours
    burning_neighbour_count = neighbourcounts[1] + neighbourcounts[7]
    candidates = (burning_neighbour_count >= 1) & unburnt_cells

    base_p = ignition_grid
    wind_grid = wind_func(wind_direction)

    # Identify which neighbours are burning
    burning_neighbors = [(neighbourstates[i] == 1) | (neighbourstates[i] == 7) for i in range(8)]

    wind_positions = [(0,1), (0,2), (1,2), (2,2), (2,1), (2,0), (1,0), (0,0)]

    wind_factor = sum(b * wind_grid[pos] for i, (b, pos) in enumerate(zip(burning_neighbors, wind_positions))) # Weighted sum of wind influence from burning neighbours

    has_water_neighbour = (neighbourcounts[3] + neighbourcounts[9]) > 0 

    # Adjust ignition probability if near water
    p = np.where(has_water_neighbour, 
                 np.minimum(base_p * 0.05 + (0.01 * wind_factor), 1.0),
                 np.minimum(base_p + (0.05 * wind_factor), 1.0))

    rand = np.random.rand(*grid.shape)
    ignite = (rand < p) & candidates
    grid[ignite] = 1

    burntgrid[burning_cells] -= 1 # Burning cells lose "burn time"
    burnt_out = (burntgrid <= 0) & burning_cells # Cells with zero burn time become fully burnt
    grid[burnt_out] = 0

    return grid


# =============================
# Supporting grids
# =============================
def make_ignition_probability_grid(map_grid):
    ignition_prob_grid = np.zeros_like(map_grid, dtype=float)
    # Set the probabilities of ignition for each terrain in the map
    ignition_prob_grid[map_grid == 2] = 0.15 #Chapparal
    ignition_prob_grid[map_grid == 3] = 0.0  #Lake
    ignition_prob_grid[map_grid == 4] = 0.02 #Dense forest
    ignition_prob_grid[map_grid == 5] = 0.7  #Canyon
    ignition_prob_grid[map_grid == 6] = 1.0  #Town
    ignition_prob_grid[map_grid == 9] = 0.0  # water cannot ignite

    return ignition_prob_grid

def make_burnt_grid(map_grid):
    burnt_grid = np.zeros_like(map_grid)
    # Set the burning times for each terrain in the map
    burnt_grid[map_grid == 2] = 108  
    burnt_grid[map_grid == 3] = 9999
    burnt_grid[map_grid == 4] = 660  
    burnt_grid[map_grid == 5] = 12  
    burnt_grid[map_grid == 6] = 400
    burnt_grid[map_grid == 9] = 9999  # water zone never burns

    return burnt_grid

# =============================
# Map
# =============================
def initialize_map():
    map = np.full((200, 200), 2)

    # Forests
    draw(map,5,12.5,5,35,4)
    draw(map,12.5,20,5,7.5,4)
    draw(map,12.5,25,25,35,4)

    #long term forest prevention
    # draw(map,0,10,35,50,4)
    # draw(map,10,30,35,42.5,4)
    # draw(map,20,30,42.5,50,4)

    # Lakes
    draw(map,17.5,20,10,20,3)
    draw(map,25,40,40,42.5,3)

    # Canyon
    draw(map,35,37.5,10,32.5,5)

    # Town
    draw(map,13.75,16.25,43.75,46.25,6)

    # Incinerator and Power Plant
    draw(map,4.5,5.5,0,1,7)
    draw(map,49,50,0,1,8)
    
    return map

# =============================
# Water Drop (Lake-like)
# =============================
def apply_water_drop_intervention(grid):
    """Apply water drop at fixed coordinates, acts as permanent lake"""
    global water_drop_info

    water_r, water_c = 150, 60  # manually defined center

    target_cells = int(WATER_AREA_KM2 / 0.0625)
    # Distance of every cell from water drop centre
    rows, cols = np.meshgrid(range(grid.shape[0]), range(grid.shape[1]), indexing='ij')
    distances = np.sqrt((rows - water_r)**2 + (cols - water_c)**2)

    # Pick the closest cells until the area is filled
    flat_distances = distances.flatten()
    sorted_indices = np.argsort(flat_distances)
    selected_indices = sorted_indices[:target_cells]

    wet = np.zeros(grid.shape, dtype=bool).flatten()
    wet[selected_indices] = True
    wet = wet.reshape(grid.shape)

    # Store information for summary output
    actual_cells = np.sum(wet)
    actual_area = actual_cells * 0.0625
    max_dist = np.max(distances[wet])

    water_drop_info = {
        "row": water_r,
        "col": water_c,
        "radius": int(max_dist),
        "area": actual_area
    }

    return wet

# =============================
# Town tracking
# =============================
def initialize_town_tracking(initial_grid):
    global town_positions_global
    town_positions_global = np.where(initial_grid == 6)

def check_town_reached(grid, step):
    global town_burn_time_global, town_positions_global
    if town_burn_time_global is not None or town_positions_global is None:
        return

    for i in range(len(town_positions_global[0])):
        r = town_positions_global[0][i]
        c = town_positions_global[1][i]
        if grid[r, c] in [0, 1]:
            town_burn_time_global = step
            hours = step * HOURS_PER_STEP
            days = hours / 24.0
            print(f"\n{'='*60}")
            print(f"TOWN REACHED at step {step}")
            print(f"Time: {hours:.1f} hours ({days:.2f} days)")
            print(f"{'='*60}\n")
            return

def print_progress(grid, step):
    if step % 10 == 0:
        burning = np.sum(grid == 1)
        burnt = np.sum(grid == 0)
        hours = step * HOURS_PER_STEP
        print(f"Step {step:3d} ({hours:.0f}h): Burning={burning:4d}, Burnt={burnt:5d}")

# =============================
# Summary
# =============================
def print_final_summary(grid, use_water):
    global town_burn_time_global, water_drop_info
    print(f"\n{'='*60}")
    print("FINAL STATISTICS")
    print(f"{'='*60}")
    print(f"Water drop: {use_water}")
    if use_water and water_drop_info:
        print(f"Water dropped at ({water_drop_info['row']}, {water_drop_info['col']})")
    if town_burn_time_global is not None:
        hours = town_burn_time_global * HOURS_PER_STEP
        days = hours / 24.0
        print(f"\nTown reached at step {town_burn_time_global}")
        print(f"Time: {hours:.1f} hours ({days:.2f} days)")
    else:
        print(f"\nTown was NOT reached")
    print(f"{'='*60}\n")

# =============================
# Enhanced transition
# =============================
def enhanced_transition(grid, neighbourstates, neighbourcounts, burntgrid, ignition_grid):
    global water_zone_global, step_count_global
    step_count_global += 1
    grid = transition_func(grid, neighbourstates, neighbourcounts, burntgrid, ignition_grid, WIND_DIRECTION)

    # water zone behaves like permanent lake
    if water_zone_global is not None:
        grid[water_zone_global] = 9

    check_town_reached(grid, step_count_global)
    print_progress(grid, step_count_global)
    return grid

# =============================
# Setup
# =============================
def setup(args):
    config_path = args[0]
    config = utils.load(config_path)
    config.title = "Wildfire Simulation"
    config.dimensions = 2

    config.states = (0,1,2,3,4,5,6,7,8,9)
    config.state_colors = [
        (0.5,0.2,0.0), (1,0.2,0), #burnt, burning
        (0.8,0.7,0.1), (0.4,0.7,1.0), #chaparral, lake
        (0.2,0.4,0.2), (1.0,1.0,0.2), #dense forest, canyon
        (0,0,0), (0.1,0.1,0.1), #town, incinerator
        (0.1,0.1,0.2), (0.2,0.6,1.0) # power plant, water
    ]

    config.num_generations = 1500
    config.grid_dims = (200,200)
    config.wrap = False
    config.initial_grid = initialize_map()
    # When the GUI pre-runs this file (File -> Open) it provides two args.
    # In that case we just save the populated config and exit so the GUI
    # can load the settings before the user presses Run.
    if len(args) == 2:
        config.save()
        sys.exit()
    return config

def setup_with_water(args):
    config = setup(args)
    config.use_water = False
    return config

# =============================
# Main
# =============================
def main_enhanced():
    global water_zone_global, step_count_global, town_burn_time_global, town_positions_global, water_drop_info
    step_count_global = 0
    town_burn_time_global = None
    water_zone_global = None
    town_positions_global = None
    water_drop_info = None

    config = setup_with_water(sys.argv[1:])
    map_grid = initialize_map()
    burntgrid = make_burnt_grid(map_grid)
    ignition_grid = make_ignition_probability_grid(map_grid)

    initialize_town_tracking(map_grid)

    if config.use_water:
        water_zone_global = apply_water_drop_intervention(map_grid)
        if water_zone_global is not None:
            map_grid[water_zone_global] = 9
            config.initial_grid = map_grid

    print("Starting simulation...\n")
    grid = Grid2D(config, (enhanced_transition, burntgrid, ignition_grid))
    timeline = grid.run()

    print_final_summary(grid.grid, config.use_water)
    config.save()
    utils.save(timeline, config.timeline_path)

if __name__ == "__main__":
    main_enhanced()