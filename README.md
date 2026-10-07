# Learner Performance Analysis (Haskell)

## Overview
This project is a Haskell program that evaluates a list of learners and reports their academic performance based on the average score of their module marks. It demonstrates core functional programming ideas such as tuple-based data modeling, list processing, sorting, filtering, and formatted console output.

The program:
- calculates the average score for each learner
- displays learners with an average of at least 80 as high achievers
- identifies the learner(s) with the highest average score, including ties
- prints results in a clear, readable format

---

## Features
- `Learner` is defined as `(String, String, [Int])`, storing the learner ID, name, and module scores.
- The dataset is stored as an immutable list named `learners`.
- `average` uses `fromIntegral` to convert integer totals into floating-point division values.
- `sortByAverage` sorts learners by average score in descending order using `sortBy` and `comparing`.
- `highAchievers` filters the list to learners whose average is 80 or above.
- `topPerformers` finds the maximum average and returns every learner tied for the highest value.
- `showLearner` formats each learner with their ID, name, scores, and average in two decimal places.
- `main` prints the results to the console using `mapM_` and `putStrLn`.

---

## Code Structure
The program in `main.hs` contains the following key parts:

- `module Main where` — entry point for the Haskell program
- imports:
  - `Data.List (maximumBy, sortBy)`
  - `Data.Ord (comparing)`
  - `Text.Printf (printf)`
- `type Learner = (String, String, [Int])`
- `learners :: [Learner]` — sample learner dataset
- `showLearner :: Learner -> String` — output formatting
- `average :: [Int] -> Double` — average calculation
- `sortByAverage :: [Learner] -> [Learner]` — descending sorting helper
- `highAchievers :: [Learner] -> [Learner]` — threshold-based filtering
- `topPerformers :: [Learner] -> [Learner]` — top-score selection with tie handling
- `main :: IO ()` — program start and output generation

---

## Program Behavior
When the program runs, it prints:

1. `High Achievers:`
   - only learners whose average score is at least 80
   - arranged from highest average to lowest

2. `Top Performer:`
   - all learners whose average equals the maximum average
   - includes all tied top scorers

---

## Haskell Concepts Used
- Pure functions for data transformation
- Pattern matching on tuples
- Higher-order functions such as `filter`, `map`, `sortBy`, and `maximum`
- Function composition and list manipulation
- I/O sequencing with `do` notation and `mapM_`

---

## How to Run
Make sure `ghc` (the Glasgow Haskell Compiler) is installed.

1. Open a terminal in the project folder.
2. Compile and run the program:

```bash
ghc main.hs -o learner_analysis
./learner_analysis
```

Alternatively, you can run it interactively with GHCi:

```bash
ghci main.hs
main
```

---

## Example Result
The dataset in `main.hs` produces a list of high achievers and identifies the top performer(s) based on average marks.


--------------------------------------------------------------------------------------

# 📘 Learner Module Eligibility System (Prolog)

This project is a Prolog-based rule system for tracking learners, their completed modules, module prerequisites, and certification eligibility. It is implemented in `main.pl` and can be queried through SWI-Prolog to answer questions such as:

- Which learners are eligible to enroll in a specific module?
- Which modules are still recommended for a learner?
- Has a learner completed all required modules for certification?

---

## 🧩 Data Model

The program defines the following facts:

- Learners: `learner(LearnerID, Name)`
- Modules: `module(ModuleName)`
- Completed modules: `completed(LearnerID, ModuleName)`
- Prerequisites: `prerequisite(ModuleName, RequiredModuleName)`
- Required modules for certification: `required_module(ModuleName)`

### Learners in the dataset

- `l001` = farhan
- `l002` = aisyah
- `l003` = ammar
- `l004` = imran
- `l005` = nurul

### Modules in the dataset

- `software_paradigm`
- `database_systems`
- `web_development`
- `data_structures`
- `programming`
- `computer_networks`

### Example completed records

```prolog
completed(l001, software_paradigm).
completed(l001, database_systems).
completed(l001, web_development).

completed(l003, software_paradigm).
completed(l003, database_systems).
completed(l003, web_development).
completed(l003, data_structures).
completed(l003, programming).
completed(l003, computer_networks).
```

---

## 📏 Rules Defined in `main.pl`

### 1. Enrollment eligibility

```prolog
eligible(Learner, Module) :-
    learner(Learner, _),
    module(Module),
    \+ (
        prerequisite(Module, Prerequisite),
        \+ completed(Learner, Prerequisite)
    ).
```

A learner is considered eligible for a module if they have already completed every prerequisite for that module.

### 2. Recommended modules

```prolog
recommend(Learner, Module) :-
    eligible(Learner, Module),
    \+ completed(Learner, Module).
```

This returns modules a learner can take next, as long as they are eligible and not yet completed.

### 3. Certification eligibility

```prolog
certification(Learner) :-
    learner(Learner, _),
    \+ (
        required_module(Module),
        \+ completed(Learner, Module)
    ).
```

A learner qualifies for certification when all required modules in the program have been completed.

---

## ⚙️ Setup and Execution

### 1. Install SWI-Prolog
Download and install [SWI-Prolog](https://www.swi-prolog.org/Download.html) for your operating system.

### 2. Save the code
Place the contents of `main.pl` in a file named `main.pl` inside your working directory.

### 3. Load the program
Open SWI-Prolog and run:

```prolog
?- [main].
```

---

## 🔍 Example Queries

After loading the file, you can ask questions such as:

```prolog
?- learner(Learner, Name).

?- eligible(l002, web_development).

?- recommend(l002, Module).

?- certification(l003).

?- required_module(Module).
```

Example output may look like:

```prolog
?- recommend(l002, Module).
Module = computer_networks ;
Module = data_structures ;
Module = programming.
```

This depends on the learner's completed modules and the prerequisite relationships defined in the database.

---

## 📝 Notes

- The project uses a rule-based approach instead of imperative code.
- It models academic progression through prerequisite logic.
- The system is easy to extend by adding more learners, modules, completed records, or new certification requirements.

----------------------------------------------------------------------------------------

# 🎓 Student Learning Pathway Dashboard

This project is a Python console application that manages student learning progress for a set of academic modules. It allows users to add learners, record completed modules and scores, check prerequisites, generate recommendations, and view a summary dashboard for all registered learners.

---

## Features

- Defines a fixed learning pathway with module prerequisites
- Validates learner ID, name, and score input
- Tracks completed modules and scores for each learner
- Calculates the average score for each learner
- Classifies performance as:
  - High Achiever
  - Good
  - Satisfactory
  - Needs Improvement
- Recommends modules that are currently eligible based on prerequisite completion
- Checks whether a learner is eligible for certification
- Displays a dashboard with:
  - total learners
  - overall average score
  - certified candidates
  - learner summary table
  - high achievers list
  - top-performing learner

---

## Learning pathway modules

The application uses these modules:

- Software Paradigm
- Database Systems
- Web Development
- Data Structures
- Programming
- Computer Networks

Prerequisites are defined as follows:

- Software Paradigm: none
- Database Systems: Software Paradigm
- Web Development: Database Systems
- Data Structures: none
- Programming: none
- Computer Networks: Web Development

---

## Requirements

- Python 3.8+
- `pandas`
- `tabulate`

---

## Installation

Install the required libraries:

```bash
pip install pandas tabulate
```

---

## How to run

From the project folder, run:

```bash
python main.py
```

Or:

```bash
py main.py
```

---

## Program flow

When the program starts, it displays a dashboard and the main menu:

```text
OPTIONS:
1. Add Learner
2. Exit
```

### Option 1: Add Learner

The program asks for:

1. Learner ID
2. Learner Name
3. For each module, whether it was completed
4. A score between 0 and 100 for each completed module

The application skips modules whose prerequisites have not yet been completed and notifies the user which prerequisite is still missing.

### Option 2: Exit

The program ends and prints a goodbye message.

---

## Notes

- Learner IDs must be unique.
- Empty IDs and names are rejected.
- Score input must be numeric and between 0 and 100.
- The dashboard sorts learners by average score from highest to lowest.
- If there are no learners, the dashboard shows an empty-state message instead of a table.

------------------------------------------------------------------------------------------
