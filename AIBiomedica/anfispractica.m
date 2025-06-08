% Supongamos que tenemos una base de datos con información de pacientes
% que incluye niveles de glucosa en sangre, la dosis de insulina requerida y si el paciente comió o no.

% Generamos datos ficticios
glucosa = [150, 140, 180, 160, 130, 145]; % Niveles de glucosa en sangre (variable de entrada)
actividad_fisica = [1, 2, 3, 2, 1, 2]; % Nivel de actividad física del paciente (variable de entrada)
dosis_insulina = [4, 3.5, 5, 4.2, 3, 3.8]; % Dosis de insulina requerida (variable de salida)

% Crear la matriz de datos
datos = [glucosa', actividad_fisica', dosis_insulina'];

% Paso 2: Entrenar el ANFIS
% Utilizaremos la función anfis de MATLAB para entrenar el ANFIS.


% Vamos a realizar inferencias utilizando nuevos datos de prueba.

% Generar nuevos datos de prueba
glucosa_prueba = [155, 165, 170]; % Nuevos niveles de glucosa en sangre
actividad_fisica_prueba = [2, 3, 1]; % Nuevos niveles de actividad física

% Realizar inferencias con el ANFIS
datos_prueba = [glucosa_prueba', actividad_fisica_prueba']; % Datos de prueba combinando niveles de glucosa y actividad física
dosis_insulina_prueba = evalfis(datos_prueba, anfis_model);

% Mostrar los resultados
disp('Resultados de dosis de insulina:');
disp(dosis_insulina_prueba);

%%
%Original: Pronóstico de COVID-19 utilizando comorbilidades 
%Comorbilidades (entradas):  0=No Padece 1=Padece
%   Obesidad
%   Hipertensión
%   Diabetes
%pronostico (salida): 0=reservado, 1=medio, 2=alto
obesidad=[0,0,0,0,1,1,1,1];
hipertension=[0,0,1,1,0,0,1,1,];
diabetes=[0,1,0,1,0,1,0,1];
pronostico=[2,0,0,0,2,1,1,0];

%matriz de datos
datosCOVID=[obesidad', hipertension',diabetes',pronostico'];
%crear ANFIS

%generar datos de prueba
obesidad_prueba=[0,0,1];
hipertension_prueba=[1,0,1];
diabetes_prueba=[1,0,0];

% Realizar inferencias con el ANFIS
datosCOVID_prueba=[obesidad_prueba',hipertension_prueba',diabetes_prueba'];
pronostico_prueba=evalfis(datosCOVID_prueba,anfis_COVID_model);

% Mostrar los resultados
disp('Pronósticos:');
disp(pronostico_prueba);