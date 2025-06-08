%Cargar la base de datos de iris/prepracion de los datos
load fisheriris;
%opcional nnstart
%Definir el porcentaje de datos para entrenamiento  prueba
trainPercentage= 0.8;
testPercentage=0.2;

%Crear un objeto cvpartition con particiones aleatorias
partition=cvpartition(species, 'Holdout', testPercentage);

%Obtener indices de entrenamiento y prueba
trainIdx=training(partition); %arreglo de n=150, con 0 y 1 solo 
testIdx=test(partition); %arreglo de n=150, con 0 y 1 solo, en donde el valor es 0 si en trainIdx es 1 y viceversa

%Dividir los datos en conjunto de entrenamiento y prueba
trainData=meas(trainIdx); %meas: entradas
trainLabels=species(trainIdx); %species: salidas o etiquetas
%trainData y trainLabels guardan el 80% de los datos de meas y species,
%respectivamente y según el índide dado en trainIdx
testData=meas(testIdx); 
testLabels=species(testIdx);
%testData y testSpecies guardan el 20% de los datos de meas y species,
%respectivamente y según el índice dadto en testIdx

 
% Preparar los datos para la entrada de la red neuronal 
% transposición de Datos
trainData = trainData.';
testData = testData.';
trainLabels = dummyvar(categorical(trainLabels)).'; %categorical: convierte datos string de trainLabels a categorías 
testLabels = dummyvar(categorical(testLabels)).'; 
%dummyvar: utiliza las categorías hechas por categorical para hacer columnas con 0 y 1, 
% en donde el 1 representa a la categoria según en donde esté posicionado en la columna
%ejemplo con testLabels, luego de haberla transformado de un arreglo de 
%datos tipo string a "testLabels = dummyvar(categorical(testLabels)).' "
%columna->...   9   10...   14  15...   25  26  
%categorías:               
% setosa  ...   1    1...    0   0...    0   0      
% versicolor ...0    0...    1   1...    0   0
% virginica ... 0    0...    0   0...    1   1
% Crear y entrenar la red neuronal
net = patternnet([10, 10]);
%
net.trainParam.show=10;
net.trainParam.epochs=500;
net.trainParam.goal=0.0001;
net.trainParam.lr=0.012;
%
net.layers{1}.transferFcn = 'radbas'; % Función de activación sigmoidea en la capa oculta
net.layers{2}.transferFcn = 'tansig';
net.layers{3}.transferFcn = 'softmax'; % Función de activación softmax en la capa de salida
net.performFcn = 'crossentropy'; % Función de rendimiento de entropía cruzada categórica
% mse mae crossentropy
net = train(net,trainData,trainLabels);

% Evaluar el rendimiento de la red neuronal en el conjunto de prueba
output = net(testData); %porcentaje de salida de las 3 posibles opciones de flor (?)
classes = vec2ind(output); %seleccion del porcentaje más alto en cada salida (?)
accuracy = sum(classes == vec2ind(testLabels)) / length(testLabels);
%sum suma todos los elementos del argumento
%classes == vec2ind(testLabels) realiza un vector con valores lógicos luego
%de comparar los elementos de classes y vec2ind(testLabels)
%vec2ind(testLabels) realiza un vector de valores según el valor más alto
%en testLabels
% Mostrar la precisión de la red neuronal
fprintf('Accuracy: %.2f%%\n', accuracy * 100);
%view(net);
%plotperform();

%%
%Tratamiento para Prediquick
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
%
net = patternnet([10, 10]);
net.trainParam.show=10;
net.trainParam.epochs=250;
net.trainParam.goal=0.0001;
net.trainParam.lr=0.012;
 
% Crear y entrenar la red neuronal
net.layers{1}.transferFcn = 'radbas'; % Función de activación sigmoidea en la capa oculta
net.layers{2}.transferFcn = 'tansig'; % Función de activación softmax en la capa de salida
net.layers{3}.transferFcn = 'softmax';
net.performFcn = 'crossentropy'; % Función de rendimiento de entropía cruzada categórica
% mse mae crossentropy
net = train(net,trainDataPQ,trainLabelsPQ);
 
% Evaluar el rendimiento de la red neuronal en el conjunto de prueba
output = net(testDataPQ);
classes = vec2ind(output);
accuracy = sum(classes == vec2ind(testLabelsPQ)) / length(testLabelsPQ);
 
% Mostrar la precisión de la red neuronal
fprintf('Accuracy: %.2f%%\n', accuracy * 100);
%%
%Parte 2 
%Base de datos: thyroid
load datasets.mat
%Definir el porcentaje de datos para entrenamiento  prueba
trainPercentagethy= 0.8;
testPercentagethy=0.2;
thyroidInputs=thyroidInputs.';
thyroidTargets=thyroidTargets.';
% inputs=vec2ind(thyroidInputs);
% targets=vec2ind(thyroidTargets);
%Crear un objeto cvpartition con particiones aleatorias
partitionthy=cvpartition(targets, 'Holdout', testPercentagethy);

%Obtener indices de entrenamiento y prueba
trainIdxthy=training(partitionthy);
testIdxthy=test(partitionthy);

%Dividir los datos en conjunto de entrenamiento y prueba
trainDatathy=thyroidInputs(trainIdxthy,:);
trainLabelsthy=thyroidTargets(trainIdxthy);

testDatathy=thyroidInputs(testIdxthy,:);
testLabelsthy=thyroidTargets(testIdxthy);


 
% Preparar los datos para la entrada de la red neuronal
trainDatathy = trainDatathy.';
testDatathy = testDatathy.';
trainLabelsthy = dummyvar(categorical(trainLabelsthy)).';
testLabelsthy = dummyvar(categorical(testLabelsthy)).';
 
% Crear y entrenar la red neuronal
net = patternnet([10]);
%
net.trainParam.show=10;
net.trainParam.epochs=1000;
net.trainParam.goal=0.001;
net.trainParam.lr=0.012;
%
net.layers{1}.transferFcn = 'logsig'; % Función de activación sigmoidea en la capa oculta
net.layers{2}.transferFcn = 'softmax'; % Función de activación softmax en la capa de salida
net.performFcn = 'crossentropy'; % Función de rendimiento de entropía cruzada categórica
% mse mae crossentropy
net = train(net,trainDatathy,trainLabelsthy);
 
% Evaluar el rendimiento de la red neuronal en el conjunto de prueba
output = net(testDatathy);
classes = vec2ind(output);
accuracy = sum(classes == vec2ind(testLabelsthy)) / length(testLabelsthy);
 
% Mostrar la precisión de la red neuronal
fprintf('Accuracy: %.2f%%\n', accuracy * 100);

%%
%Crear un datastore para todos los datos MNIST
mnistData=digitDatastore;
a=readimage(mnistData,10000);
imshow(a);
%Dividir los datos en datos de entrenamiento y prueba
[trainData, testData]=splitEachLabel(mnistData, 0.7, 'randomized');
%Converir datos de entrenamiento en una matriz y un vector
trainImages=zeros([28 28 1 numel(trainData.Files)]);
trainLabels=categorical(trainData.Labels);
for i=1:numel(trainData.Files)
    trainImages(:,:,1,i)=readimage(trainData,i);
end
hiddenSize=50;
outputSize=15;
net=patternnet(hiddenSize);
net=train(net,reshape(trainImages, [], numel(trainData.Files)), dummyvar(trainLabels)');
