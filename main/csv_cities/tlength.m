sol(end+1)=sol(1);
dist=0;
for p=1:20
    x=vec(sol(p+1),1)-vec(sol(p),1);
    y=vec(sol(p+1),2)-vec(sol(p),2);
    r=sqrt(x^2+y^2);
    dist=dist+r;
end