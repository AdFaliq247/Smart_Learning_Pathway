% Learners (ID, name)

learner(l001, farhan).
learner(l002, aisyah).
learner(l003, imran).
learner(l004, ammar).
learner(l005, nurul).

% Modules (ID, modulename)

module(m100, software_paradigm).
module(m200, database_systems).
module(m300, web_development).
module(m400, data_structures).
module(m500, programming).
module(m600, computer_networks).

% Learner that completed the module (LearnerID, ModuleID)

% Learner Farhan
completed(l001, m100).
completed(l001, m200).

% Learner Aisyah
completed(l002, m100).
completed(l002, m200).

% Learner Imran
completed(l003, m100).
completed(l003, m200).
completed(l003, m300).

% Learner Ammar
completed(l004, m100).
completed(l004, m200).
completed(l004, m300).
completed(l004, m400).
completed(l004, m500).
completed(l004, m600).

% Learner Nurul
completed(l005, m100).
completed(l005, m200).
completed(l005, m300).
completed(l005, m400).
completed(l005, m500).
completed(l005, m600).

% Prerequisites (ModuleID, RequiredModuleID)

prerequisite(m200, m100). 
prerequisite(m300, m200). 
prerequisite(m500, m300). 


% Required module 

required_module(m100). 
required_module(m200). 
required_module(m300). 
required_module(m400). 
required_module(m500). 
required_module(m600).


% Check if learner is eligible to enroll

eligible(Learner, Module) :-
    learner(Learner, _),
    module(Module, _),
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

