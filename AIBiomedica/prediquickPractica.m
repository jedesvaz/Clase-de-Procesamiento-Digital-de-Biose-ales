%prediquick=readtable("prediquick.csv");
%doc prediquick;
%[x,y]=prediquick;
%%x=x';
%%y=y';

%y2=vec2ind(y')';

%%o=[x,y];
%scatter(x(:,1),y2,'filled');colormap(jet(3));
%scatter(x(:,1),(x(:,2),50,y2,'filled');colormap(jet(3));
%scatter3(x(:,1),(x(:,2),(x(:,3),50,y2,'filled');colormap(jet(3));
%plotmatrix(x);colormap(jet(3));
%prediquick2=table2array(prediquick);

% Cargar los datos
prediquick=readtable('prediquick');
[sujetos, variables]=size(prediquick);
datos=table2array(prediquick(:,2:end));