-- Module Declaration: defines the entry point of the program
module Main where

    -- Importing maximumBy: a higher-order function to find the maximum element in a list
    -- Importing sortBy: a higher-order function to sort a list based on a custom comparison
    import Data.List (maximumBy, sortBy)

    -- Importing comparing: used with maximumBy to compare learners by average score
    import Data.Ord (comparing)

    -- Importing printf: used to format numeric output (e.g., averages) to fixed decimal places
    import Text.Printf (printf)

    -- Type Definition: Learner is represented as a tuple (ID, Name, Scores)
    type Learner = (Int, String, [Int])

    -- Immutable dataset: list of learners with IDs, names, and module scores
    learners :: [Learner]
    learners =
        [
            (1, "Farhan", [85, 90, 78]),
            (2, "Aisyah", [95, 92, 96]),
            (3, "Ammar", [95, 92, 96]),
            (4, "Imran", [80, 80, 80]),
            (5, "Nurul", [60, 75, 70])
        ]

    -- Function to format learner details into a readable string
    -- Demonstrates pattern matching by unpacking tuple values
    -- Uses printf to limit average output to two decimal places
    showLearner :: Learner -> String
    showLearner (id, name, scores) = 
        "[ID:" ++ show id ++ "] " ++ name ++ " -> Scores: " ++ show scores
        ++ " | Average: " ++ printf "%.2f" (average scores) 

    -- Pure function to calculate average score
    -- Uses fromIntegral to convert Int to Double for precise division
    average :: [Int] -> Double
    average scores = fromIntegral (sum scores) / fromIntegral (length scores)

    -- Helper: sort learners by average score in descending order
    -- flip is used to reverse the order for descending sort
    sortByAverage :: [Learner] -> [Learner]
    sortByAverage = sortBy (flip (comparing (\(_, _, scores) -> average scores)))

    -- highAchievers: filter selects learners with average >= 80
    -- highAchievers is sorted by average score in descending order using sortByAverage
    highAchievers :: [Learner] -> [Learner]
    highAchievers ls = 
        let achievers = filter (\(_, _, scores) -> average scores >= 80) ls
        in sortByAverage achievers

    -- Top performer: finds learners with the highest average score
    -- Handles ties by returning all learners with the same top average
    -- topPerformers is sorted in descending order (though all will have the same average)
    topPerformers :: [Learner] -> [Learner]
    topPerformers ls= 
        let maxAvg = maximum (map (\(_, _, scores) -> average scores) ls)
            tied = filter (\(_, _, scores) -> average scores == maxAvg) ls
        in sortByAverage tied

    -- Main function: program execution starts here
    -- Outputs highAchievers and topPerformers in readable format
    -- Uses putStrLn instead of print to avoid extra quotation marks around strings
    -- Uses mapM_ to apply putStrLn to each learner in the lists
    -- giving clean output without brackets or commas
    main :: IO ()
    main = do
        putStrLn ("\nHigh Achievers: ")
        mapM_ (putStrLn . showLearner) (highAchievers learners)
        putStrLn ("\nTop Performer: ")
        mapM_ (putStrLn . showLearner) (topPerformers learners)
