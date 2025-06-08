%crear FIS
tipFIS=mamfis(...
    'name','fuzzy tipping',...
    'numinputs',2,'numinputMFs',3,...
    'numoutputs',1,'numoutputMFs',3,...
    'addrule','none'...
    );

%actualizar entrada 1
tipFIS.Inputs(1).name='servicio';
tipFIS.Inputs(1).Range=[0 10];
tipFIS.Inputs(1).MembershipFunctions(1).Name='pobre';
tipFIS.Inputs(1).MembershipFunctions(1).Type='gaussmf';
tipFIS.Inputs(1).MembershipFunctions(1).Parameters=[1.5 0];
tipFIS.Inputs(1).MembershipFunctions(2).Name='buena';
tipFIS.Inputs(1).MembershipFunctions(2).Type='gaussmf';
tipFIS.Inputs(1).MembershipFunctions(2).Parameters=[1.5 5];
tipFIS.Inputs(1).MembershipFunctions(3).Name='excelente';
tipFIS.Inputs(1).MembershipFunctions(3).Type='gaussmf';
tipFIS.Inputs(1).MembershipFunctions(3).Parameters=[1.5 10];

%actualizar entrada 2
tipFIS.Inputs(2).name='food';
tipFIS.Inputs(2).Range=[0 10];
tipFIS.Inputs(2).MembershipFunctions(1).Name='rancio';
tipFIS.Inputs(2).MembershipFunctions(1).Type='trapmf';
tipFIS.Inputs(2).MembershipFunctions(1).Parameters=[0 0 2 4];
tipFIS.Inputs(2).MembershipFunctions(2).Name='bien';
tipFIS.Inputs(2).MembershipFunctions(2).Type='trapmf';
tipFIS.Inputs(2).MembershipFunctions(2).Parameters=[2 4 6 8];
tipFIS.Inputs(2).MembershipFunctions(3).Name='delicioso';
tipFIS.Inputs(2).MembershipFunctions(3).Type='trapmf';
tipFIS.Inputs(2).MembershipFunctions(3).Parameters=[6 8 10 10];


%actualizar salida
tipFIS.Outputs(1).Name='propina';
tipFIS.Outputs(1).Range=[0 30];
tipFIS.Outputs(1).MembershipFunctions(1).Name='baja';
tipFIS.Outputs(1).MembershipFunctions(1).Type='trimf';
tipFIS.Outputs(1).MembershipFunctions(1).Parameters=[0 5 15];
tipFIS.Outputs(1).MembershipFunctions(2).Name='promedio';
tipFIS.Outputs(1).MembershipFunctions(2).Type='trimf';
tipFIS.Outputs(1).MembershipFunctions(2).Parameters=[5 15 25];
tipFIS.Outputs(1).MembershipFunctions(3).Name='alta';
tipFIS.Outputs(1).MembershipFunctions(3).Type='trimf';
tipFIS.Outputs(1).MembershipFunctions(3).Parameters=[15 25 30];

subplot(3,1,1)
plotmf(tipFIS,'input',1,1000);
subplot(3,1,2)
plotmf(tipFIS,'input',2,1000);
subplot(3,1,3)
plotmf(tipFIS,'output',1,1000);

%especificas reglas difusas
rules=[...
    "If servicio is pobre or food is rancio then propina is baja";...
    "If servicio is buena then propina is promedio";...
    "If servicio is excelente or food is delicioso then propina is alta"...
    ];
figure
tipFIS=addRule(tipFIS,rules);
gensurf(tipFIS)

%agregar nuevas reglas
new_rule="If food is bien then propina is alta";
tipFIS=addRule(tipFIS,new_rule);
figure
gensurf(tipFIS);
%%
%PRONOSTICO DE COVID-19 CON BASE EN COMORBILIDADES
covidFIS=mamfis(...
    'name','fuzzy COVID-19',...
    'numinputs',3,'numinputMFs',2,...
    'numoutputs',1,'numoutputMFs',3,...
    'addrule','none'...
    );

%actualizar entrada 1
covidFIS.Inputs(1).name='diabetes';
covidFIS.Inputs(1).Range=[0 10];
covidFIS.Inputs(1).MembershipFunctions(1).Name='No Padece';
covidFIS.Inputs(1).MembershipFunctions(1).Type='gaussmf';
covidFIS.Inputs(1).MembershipFunctions(1).Parameters=[1.5 2.5];
covidFIS.Inputs(1).MembershipFunctions(2).Name='Padece';
covidFIS.Inputs(1).MembershipFunctions(2).Type='gaussmf';
covidFIS.Inputs(1).MembershipFunctions(2).Parameters=[1.5 7.5];

%actualizar entrada 2
covidFIS.Inputs(2).name='hipertension';
covidFIS.Inputs(2).Range=[0 10];
covidFIS.Inputs(2).MembershipFunctions(1).Name='No Padece';
covidFIS.Inputs(2).MembershipFunctions(1).Type='trapmf';
covidFIS.Inputs(2).MembershipFunctions(1).Parameters=[0 0 2.5 5];
covidFIS.Inputs(2).MembershipFunctions(2).Name='Padece';
covidFIS.Inputs(2).MembershipFunctions(2).Type='trapmf';
covidFIS.Inputs(2).MembershipFunctions(2).Parameters=[5 7.5 10 10];

%actualizar entrada 3
covidFIS.Inputs(3).name='obesidad';
covidFIS.Inputs(3).Range=[0 10];
covidFIS.Inputs(3).MembershipFunctions(1).Name='No Padece';
covidFIS.Inputs(3).MembershipFunctions(1).Type='gaussmf';
covidFIS.Inputs(3).MembershipFunctions(1).Parameters=[1.5 2.5];
covidFIS.Inputs(3).MembershipFunctions(2).Name='Padece';
covidFIS.Inputs(3).MembershipFunctions(2).Type='gaussmf';
covidFIS.Inputs(3).MembershipFunctions(2).Parameters=[1.5 7.5];

%actualizar salida
covidFIS.Outputs(1).Name='Pronóstico';
covidFIS.Outputs(1).Range=[0 30];
covidFIS.Outputs(1).MembershipFunctions(1).Name='reservado';
covidFIS.Outputs(1).MembershipFunctions(1).Type='trimf';
covidFIS.Outputs(1).MembershipFunctions(1).Parameters=[0 5 15];
covidFIS.Outputs(1).MembershipFunctions(2).Name='medio';
covidFIS.Outputs(1).MembershipFunctions(2).Type='trimf';
covidFIS.Outputs(1).MembershipFunctions(2).Parameters=[5 15 25];
covidFIS.Outputs(1).MembershipFunctions(3).Name='alto';
covidFIS.Outputs(1).MembershipFunctions(3).Type='trimf';
covidFIS.Outputs(1).MembershipFunctions(3).Parameters=[15 25 30];

subplot(4,1,1)
plotmf(covidFIS,'input',1,1000);
subplot(4,1,2)
plotmf(covidFIS,'input',2,1000);
subplot(4,1,3)
plotmf(covidFIS,'input',3,1000);
subplot(4,1,4)
plotmf(covidFIS,'output',1,1000);

%especificas reglas difusas
rules=[...
    "If diabetes is Padece or hipertension is Padece then Pronóstico is reservado";...
    "If hipertension is Padece and obesidad is Padece then Pronóstico is medio";...
    "If obesidad is Padece and diabetes is Padece then Pronóstico is medio";...
    "If obesidad is Padece then Pronóstico is alto"...
    ];
figure
covidFIS=addRule(covidFIS,rules);
opt=gensurfOptions;
opt.InputIndex = [1 2];
gensurf(covidFIS, opt);
opt.InputIndex = [1 3];
gensurf(covidFIS, opt);
opt.InputIndex = [2 3];
gensurf(covidFIS, opt);