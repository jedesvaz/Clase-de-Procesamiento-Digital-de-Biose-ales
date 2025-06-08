%%ejemplo
doc iris_dataset;
[x,y]=iris_dataset;
x=x';
y=y';

y2=vec2ind(y')';

o=[x,y2];
scatter(x(:,1),y2,'filled');colormap(jet(3));
scatter(x(:,1),(x(:,2),50,y2,'filled');colormap(jet(3));
scatter3(x(:,1),(x(:,2),(x(:,3),50,y2,'filled');colormap(jet(3));
plotmatrix(x);colormap(jet(3));
