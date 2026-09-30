% Learners (ID, name)

learner(l001, farhan).
learner(l002, aisyah).
learner(l003, ammar).
learner(l004, imran).
learner(l005, nurul).

% Modules (modulename)

module(software_paradigm).
module(database_systems).
module(web_development).
module(data_structures).
module(programming).
module(computer_networks).

% Learner that completed the module (LearnerID, ModuleID)

% Learner Farhan
completed(l001, software_paradigm).
completed(l001, database_systems).
completed(l001, web_development).


% Learner Aisyah
completed(l002, software_paradigm).
completed(l002, database_systems).
completed(l002, web_development).


% Learner Ammar
completed(l003, software_paradigm).
completed(l003, database_systems).
completed(l003, web_development).
completed(l003, data_structures).
completed(l003, programming).
completed(l003, computer_networks).


% Learner Imran
completed(l004, software_paradigm).
completed(l004, database_systems).
completed(l004, web_development).
completed(l004, data_structures).
completed(l004, programming).
completed(l004, computer_networks).

% Learner Nurul
completed(l005, software_paradigm).
completed(l005, database_systems).
completed(l005, web_development).
completed(l005, data_structures).
completed(l005, programming).
completed(l005, computer_networks).

% Prerequisites (ModuleID, RequiredModuleID)

prerequisite(database_systems, software_paradigm0). 
prerequisite(web_development, database_systems). 
prerequisite(computer_networks, web_development). 


% Required module 

required_module(software_paradigm). 
required_module(database_systems). 
required_module(web_development). 
required_module(data_structures). 
required_module(programming). 
required_module(computer_networks).


% Check if learner is eligible to enroll

eligible(Learner, Module) :-
    learner(Learner, _),
    module(Module),
    \+ (
        prerequisite(Module, Prerequisite),
        \+ completed(Learner, Prerequisite)
    ).


% Recommended module for learner

recommend(Learner, Module) :-
    eligible(Learner, Module),
    \+ completed(Learner, Module).



% Learner that eligible for certification

certification(Learner) :-
    learner(Learner, _),
    \+ (
        required_module(Module),
        \+ completed(Learner, Module)
    ).

