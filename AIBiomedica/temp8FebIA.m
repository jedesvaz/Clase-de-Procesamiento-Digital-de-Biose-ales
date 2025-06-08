% Cargar los datos
datos_abiertos_covid19__=readtable('datos_abiertos_covid19__');
[sujetos, variables]=size(datos_abiertos_covid19__);
datos=table2array([datos_abiertos_covid19__(:,4:10),datos_abiertos_covid19__(:,14:37),datos_abiertos_covid19__(:,39:end)]);
%tabla1_d_k=[datos_abiertos_covid19__(:,4:10)];

%tabla1_d_k=[datos_abiertos_covid19__(:,4:10)];
%datos=table2array(tabla1_d_k);
% tabla_n_al=[datos_abiertos_covid19__(:,14:37)];
% tabla_am_an=[datos_abiertos_covid19__(:,39:end)];
% tablaRecortada=[tabla1_d_k, tabla_n_al, tabla_am_an];

for i=1:33
    subplot(7,5,i);
    histogram(datos(:,i));
end;


%Análisis de multicolinealidad
corr = corrcoef(datos);
figure;
imagesc(corr);
colorbar;