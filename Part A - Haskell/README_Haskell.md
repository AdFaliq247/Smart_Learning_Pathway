# Learner Performance Analysis (Haskell)

## 📖 Overview
This project is a simple Haskell program that analyzes a dataset of learners and their module scores.  
It demonstrates functional programming concepts such as **pattern matching**, **higher-order functions**, **list processing**, and **IO actions**.

The program:
- Calculates the average score for each learner.
- Displays **high achievers** (average ≥ 80) sorted in descending order.
- Identifies **top performers**, handling ties when multiple learners share the highest average.
- Outputs results in a clean, readable format.

---

## 🛠 Features
- **Immutable dataset**: Learners are stored as tuples `(ID, Name, Scores)`.
- **Average calculation**: Pure function using `fromIntegral` for precise division.
- **Sorting**: Uses `sortBy` with `flip comparing` to order learners by average score (highest first).
- **Filtering**: Selects learners meeting performance thresholds.
- **Tie handling**: Ensures multiple top performers are displayed if averages are equal.
- **Formatted output**: Uses `printf` to show averages with two decimal places.
- **Clean printing**: Uses `mapM_` to run `putStrLn` on each learner, avoiding extra brackets or quotes.

---

## 📂 Code Structure
- `Learner` type: `(Int, String, [Int])`
- `learners`: Sample dataset of 5 learners.
- `showLearner`: Formats learner details into a readable string.
- `average`: Calculates average score from a list of integers.
- `sortByAverage`: Helper to sort learners by average (descending).
- `highAchievers`: Filters learners with average ≥ 80 and sorts them.
- `topPerformers`: Finds learners with the highest average, includes ties, and sorts them.
- `main`: Entry point that prints results to the console.

---

## ▶️ Example Output
High Achievers:
[ID:2] Aisyah -> Scores: [95,92,96] | Average: 94.33
[ID:3] Ammar -> Scores: [95,92,96] | Average: 94.33
[ID:1] Farhan -> Scores: [85,90,78] | Average: 84.33
[ID:4] Imran -> Scores: [80,80,80] | Average: 80.00

Top Performer(s):
[ID:2] Aisyah -> Scores: [95,92,96] | Average: 94.33
[ID:3] Ammar -> Scores: [95,92,96] | Average: 94.33



---

## 💡 Key Concepts Demonstrated
- **Functional purity**: `average` is a pure function with no side effects.
- **Higher-order functions**: `filter`, `map`, and `sortBy` are used extensively.
- **Declarative style**: Logic is expressed directly through function composition.
- **IO sequencing**: `mapM_` ensures printing actions run sequentially and discard results.

---

## 🚀 How to Run
1. Save the code in a file named `main.hs`.
2. Open GHCi (Glasgow Haskell Compiler interactive environment).
3. Load the file:
   ```bash
   ghci main.hs

4. run the program:
    main

