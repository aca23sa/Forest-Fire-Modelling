# COM 3524 – System Tools

This repository contains the source code and documentation for the system tools developed for the COM3524 course. 

## Features

- Cross-platform support (Linux, macOS, Windows)
- Modular, extensible design for course assignments

---
## Prerequisites
Before starting, ensure the following softwares and tools are installed on your machine:

- [Python 3.8+](https://www.python.org/downloads/)
- `pip` (Python package manager for installing necessary dependencies)
- Git (to clone this repository)


###  Docker Desktop
Download and install Docker Desktop:  
[https://www.docker.com/products/docker-desktop/]

###  X11 Server
| Platform | Tool     | Link                                      |
|----------|----------|-------------------------------------------|
| Windows  | VcXsrv   | [VcXsrv Download](https://sourceforge.net/projects/vcxsrv/) |
| macOS    | XQuartz  | [XQuartz Download](https://www.xquartz.org/) |
| Linux    | Built-in | Usually pre-installed with the system     |

---

---

## Installation

### 1. Clone the Repository
Clone this repository and navigate to the COM3524 folder:

```bash
git clone https://github.com/ac1asana/COM3524.git
cd COM3524
```
---

>[!NOTE]
>Before running the tools make sure that you have the latest update of this repository by typing **git pull**.

## Platform-Specific Notes
---

## Windows Instructions

### 1. **Install Required Software**
- Install Docker Desktop and VcXsrv as mentioned [above](#Prerequisites)

### 2.1. Run Docker and X Server in the background
After installing VcXsrv software, run the server (Xlaunch)
Set the default display settings as follow:
  - Multiple windows mode
  - Start no client
  - **Disable access control**
 
<p align="center">
  <img src="https://github.com/user-attachments/assets/aaef6bd4-151b-4dfa-b957-66b3f91aa650" width="48%" />
  <img src="https://github.com/user-attachments/assets/c83ba456-e844-4454-ae72-5dc283f863fc" width="48%" />
  <img src="https://github.com/user-attachments/assets/157322a4-18c8-460b-b2b7-773d6bc17a61" width="48%" />
</p>

- Once the configuration is completed, a small X symbol will appear on the bottom right panel of your screen:

<p align="center">
  <img src="https://github.com/user-attachments/assets/c56ef8b4-db6e-419e-8f5b-02251e338761" width="45%" />
</p>

- This confirms that the X server is running in the background.

### 2.2. Edit the script to add your local path
Next, open the script (linux.sh, mac.sh or windows.bat) which you will be running based on your operating system and replace this line **/Users/ayesha/Desktop/COM3524** with the full path on your own local directory where you have cloned this repository.

### 3. Run the script
Once you have made sure that the previous steps are done, you are ready to run the script:

```bash
.\windows.bat
```
After running the script, a shell **root@com3524:/src#** opens inside the container.
Inside that shell, start the tools menu with: 

```bash
python run_tool.py 
```
---
>[!NOTE]
>Make sure that docker is running in the background 

## Linux (Ubuntu) Instructions

>[!NOTE]
>No additional configuration is typically required. Make sure you have Python and `pip` installed:
>run the command `python3 --version` or `pip --version` to check whether it is installed on your system

### 1. **Install Docker**

Follow Docker’s official guide:  
[https://docs.docker.com/engine/install/ubuntu](https://docs.docker.com/engine/install/ubuntu)

### 2. **Set Up Repository and Test Docker**
```bash
sudo docker run hello-world
```

### 3. Fix Permission Denied Errors (Optional)
If you encounter permission errors:  
[Fix Docker Permission Denied](https://hostinger.com/tutorials/how-to-fix-docker-permission-denied-error)

### 4. **Run the following script**
```bash
./linux.sh 
```
---

## MacOS

Ensure Python 3 is installed (macOS may come with Python 2.x by default):

```bash
brew install python
```

### 1. Use the Zsh Shell
Check with:
```bash
echo $SHELL
```
Switch to `zsh` if needed:
```bash
chsh -s /bin/zsh
```

### 2. **Deactivate Conda (if active)**
```bash
conda deactivate
```

### 3. **Install and Launch XQuartz**
- Install from: [https://www.xquartz.org/](https://www.xquartz.org/)
- After installing, **restart your computer**
- Launch XQuartz and enable network connections:
  - Settings → Security → Check **"Allow connections from network clients"**


### 4. **Run the following script**
```bash
./mac.sh 
```

After running the script, a shell **root@com3524:/src#** opens inside the container.
Inside that shell, start the tools menu with: 

```bash
python run_tool.py 
```
---

Once you run the command, the following menu should appear, allowing you to select which tool to launch.

<div style="display: flex; align-items: flex-start; gap: 1rem;">

  <img src="https://github.com/user-attachments/assets/62b99fdb-c21e-4d47-add8-1b6166f2dda6" alt="Tools Menu Screenshot" width="500" style="border-radius: 8px;">
</div>

  - The menu allows you to select from available tools.
  - Use the number keys (1–3) to choose the desired tool.  
  - Once selected, the corresponding interface (GUI or web) will open. 

##  Troubleshooting

- **GUI doesn't appear?**
  - Ensure X server is running
  - Check that `DISPLAY` is correctly set

- **Permission denied**
  - Ensure user is added to Docker group, or run using `sudo`

- Ensure you’re using **Python 3.8 or higher**.
- For permission errors on Linux/macOS, try using `sudo` if needed.
- On Windows, run the command prompt or PowerShell as Administrator if access is denied.

---


## Editing code in VS Code
- Open VS Code
- Click the bottom left double arrows icon
- Select **Attach to Running Container**
- Choose the container named **com3524**
- Next open folder named /src and now it should show all your files within the container you can eaily edit

>[!NOTE]
>Make sure that your container is running and you are in the interactive shell


## Stopping the container
- Once you are done using the tools, type
```bash
exit 
```
inside the container shell

- To remove container completely, run:
```bash
docker rm com3524 
```

## Running tools outside Docker environment
- If you encounter issues running the tools in the Docker environment, you can follow these instructions to run them directly.

- Navigate to the cloned repository using `cd` and run the following command 
```bash
python run_tool.py
```

## Author
Ayesha Sana, Department of Computer Science  
