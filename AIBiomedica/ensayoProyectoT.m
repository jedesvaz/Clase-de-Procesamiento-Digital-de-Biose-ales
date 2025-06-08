%cargar los datos
datosCovid=readtable('datos_abiertos_covid19__.csv');
[sujetos,variables]=size(datosCovid);

datos= table2array(datosCovid(:,[3:10,14:35,39:end,36]));
%visualización de los datos
% figure;
% subplot(2,2,1);
% histogram(datos(:,1));
% title ('variable 1');
% subplot(2,2,2);
% histogram(datos(:,2));
% title('variable 2');%...(otras variables)
% subplot(2,2,3);
% scatter(datos(:,1), datos(:,2));
% title('relación entre variable 1 y 2');% (otras relaciones)
for i=1:32
    subplot(4,8,i);
    histogram(datos(:,i));
end
maximos= max(datos);
contador=1;
figure;
for j=1:32
    if maximos(1,j)>2
        subplot(8,4,contador);
        boxplot(datos(:,j));
        title('Variable'+j);
        contador=contador+1;
    end
end

% Dibujar gráficos de caja
figure;
subplot(2,2,1);
boxplot(datos(:, 1)); %identificación de datos atópicos (50% de los datos están dentro de los cuartiles)
title('Variable 1');
subplot(2,2,2);
boxplot(datos(:, 2));
title('Variable 2');
%...(otras variables) %normalización de los datos
datos_norm = (datos - mean(datos)) ./ std(datos);%análisis de muticonlinealidad
corr=corrcoef(datos_norm);
figure;
imagesc(corr);
colorbar;
%%
%datos=table2array(prediquick);
X = datos(:,2:end-1);
Y = datos(:,end);
cv = cvpartition(Y,'Holdout',0.3);
Xtrain = X(training(cv),:);
Ytrain = Y(training(cv));
Xtest = X(test(cv),:);
Ytest = Y(test(cv));
% regresion lineal
% Entrenamiento del modelo de regresión lineal
model = fitlm(Xtrain, Ytrain);
% Hacer predicciones con el modelo entrenado
y_pred = predict(model, Xtest);
% Calcular el error de las predicciones
error = mean(abs(y_pred - Ytest));
%% regresión logística
% Entrenar el modelo de regresión logística
mdl = fitglm(Xtrain, Ytrain, 'Distribution','binomial');% Realizar predicciones sobre el conjunto de prueba
yhat = predict(mdl,Xtest);
error2 = mean(abs(yhat - Ytest));
%% Árboles de decisión
% Creae el objeto de clasificador Árboles de decisión
tree = fitctree(Xtrain,Ytrain);
% Realizar predicciones sobre el conjunto de prueba
yhat = predict(tree, Xtest);
error3 = mean(abs(yhat - Ytest));
%% nuevo DS
dataXtrain=[Xtrain(:,2),Xtrain(:,13),Xtrain(:,22)];
dataXtest=[Xtest(:,2),Xtest(:,13),Xtest(:,22)];
%% 2.Fitting method
%b=stepwisefit(X,Y);
[b,se,pval,finalmodel,stats]=stepwisefit(X,Y);
cont=1;
for i=1:61
    if finalmodel(i)==1
        var(cont)=i;
        var2Xtrain(:,cont)=Xtrain(:,i);
        var3Xtest(:,cont)=Xtest(:,i);
        cont=cont+1;
    end
end
%%
prediquick=readtable('prediquick');
[sujetos, variables]=size(prediquick);
datos=table2array(prediquick(:,2:end));
diagnostics=datos(:,end);
%Definir el porcentaje de datos para entrenamiento  prueba
trainPercentagePQ= 0.8;
testPercentagePQ=0.2;

%Crear un objeto cvpartition con particiones aleatorias
partitionPQ=cvpartition(diagnostics, 'Holdout', testPercentagePQ);

%Obtener indices de entrenamiento y prueba
trainIdxPQ=training(partitionPQ);
testIdxPQ=test(partitionPQ);

%Dividir los datos en conjunto de entrenamiento y prueba
trainDataPQ=datos(trainIdxPQ);
trainLabelsPQ=diagnostics(trainIdxPQ);

testDataPQ=datos(testIdxPQ);
testLabelsPQ=diagnostics(testIdxPQ);

% Preparar los datos para la entrada de la red neuronal
trainDataPQ = trainDataPQ.';
testDataPQ = testDataPQ.';
trainLabelsPQ = dummyvar(categorical(trainLabelsPQ)).';
testLabelsPQ = dummyvar(categorical(testLabelsPQ)).';
%% 
% Crear y entrenar la red neuronal
net = patternnet([10, 10]);
net.layers{1}.transferFcn = 'poslin'; % Función de activación sigmoidea en la capa oculta
net.layers{2}.transferFcn = 'poslin'; % Función de activación softmax en la capa de salida
net.layers{3}.transferFcn = 'poslin';
net.performFcn = 'crossentropy'; % Función de rendimiento de entropía cruzada categórica
% mse mae crossentropy
net = train(net,trainDataPQ,trainLabelsPQ);
 
% Evaluar el rendimiento de la red neuronal en el conjunto de prueba
output = net(testDataPQ);
classes = vec2ind(output);
accuracy = sum(classes == vec2ind(testLabelsPQ)) / length(testLabelsPQ);
 
% Mostrar la precisión de la red neuronal
fprintf('Accuracy: %.2f%%\n', accuracy * 100);