import pandas as pd
from tabulate import tabulate
# List of modules in the learning pathway
modules = [
    "Software Paradigm",
    "Database Systems",
    "Web Development",
    "Data Structures",
    "Programming",
    "Computer Networks"
]

# Prerequisite facts for each module
prerequisite_facts = {
    "Software Paradigm": [],
    "Database Systems": ["Software Paradigm"],
    "Web Development": ["Database Systems"],
    "Data Structures": [],
    "Programming": ["Web Development"],
    "Computer Networks": []
}

# Check if learner can take a module
def prequisites_checking(module, modules_done):

    prerequisites = prerequisite_facts.get(module, [])

    for prereq in prerequisites:
        if prereq not in modules_done:
            return False

    return True

# Recommend modules for the learner
def recommend_modules(modules_done):

    recommendations = []

    for module in modules:

        if module not in modules_done:

            if prequisites_checking(module, modules_done):
                recommendations.append(module)

    return recommendations

# Calculate average score
def calculate_average(scores):
    
    if scores:
        total = sum(scores)
        average = total / len(scores)
        return average
    else:
        return 0.0

# Helper function to classify learner performance
def classify_performance(average):

    if average >= 80:
        return "High Achiever"
    elif average >= 70:
        return "Good"
    elif average >= 60:
        return "Satisfactory"
    else:
        return "Needs Improvement"

# Learner class with input validation and methods to get average, classification, recommendations, and certification status
class Learner:

    def __init__(self, id_num, name, scores, modules_done):

        if  id_num == '':
            print("ID cannot be empty.")

        if name == '':
            print("Name cannot be empty.")

        if len(scores) != len(modules_done):
            print("Scores and modules count must must match.")

        for score in scores:

            if score < 0 or score > 100:
                print("Scores must be between 0 and 100.")


        self.id_num = id_num
        self.name = name
        self.scores = scores
        self.modules_done = modules_done

    # Get learner average from pure helper function calculate_average
    def get_average(self):

        return calculate_average(self.scores)

    # Get learner classification
    def get_classification(self):

        return classify_performance(self.get_average())

    # Get recommended modules from pure helper function recommend_modules
    def get_recommendations(self):

        return recommend_modules(self.modules_done)

    # Check certification status
    def get_certification_status(self):

        if all( module in self.modules_done for module in modules):
            return "Eligible"
        else:
            return "Not Eligible"

# List to store learners
learners = []


# Get high achieving learners using filter and lambda function
def get_high_achievers(learner_list):

    return list(filter( lambda learner: learner.get_classification() == "High Achiever", learner_list))


# Get single top-performing learner using map, max and filter functions
def get_top_learner(learner_list):

    if not learner_list:
        return None

    # Go through the learners average scores using map then using the max function to find the highest average score
    highest_average = max(map(lambda learner: learner.get_average(), learner_list))

    # Filter the learners to find those with the highest average score using filter and lambda function
    top_learners = list(filter(lambda learner: learner.get_average() == highest_average, learner_list))
    # If there is two learner were have the same average, it will return the first one in the list
    return top_learners[0]




# Display dashboard for learners with summary statistics and tables
def display_dashboard(learner_list):

    print("\n" + "=" * 80)
    print("STUDENT LEARNING PATHWAY DASHBOARD")
    print("=" * 80)

    if not learner_list:

        print("Total Learners Registered : 0")
        print("Overall Average Score     : N/A")
        print("Certified Candidates      : 0")
        print("-" * 80)
        print("No learner records found. Please select Option 1 to add Learner.")
        print("=" * 80)

        return

    data = []

    # Loop through learners to prepare data for the dashboard
    for learner in learner_list:

        recommendations = learner.get_recommendations()

        data.append({
            "ID": learner.id_num,
            "Name": learner.name,
            "Average": round(learner.get_average(), 2),
            "Category": learner.get_classification(),
            "Completed": len(learner.modules_done),
            "Recommended": ", ".join(recommendations) if recommendations else "None",
            "Certification": learner.get_certification_status()
        })

    # Create a DataFrame for the dashboard
    df = pd.DataFrame(data)

    df = df.sort_values(by="Average", ascending=False)

    print(f"Total Learners Registered: {len(df)}")  

    average = df['Average'].mean()
    print(f"Overall Average Score: {average:.2f}")

    certified = (df['Certification'] == 'Eligible').sum()
    print(f"Certified Candidates: {certified}")

    print("-" * 80)
    # Learner summary table
    print("LEARNER SUMMARY TABLE".center(80))
    print(tabulate(df, headers="keys",tablefmt="psql",showindex=False))

    # Append high achievers to the into dataframe and display them in  High Achievers Table
    high_achievers = get_high_achievers(learner_list)

    if high_achievers:

        high_achiever_data = []

        for learner in high_achievers:

            high_achiever_data.append({
                "ID": learner.id_num,
                "Name": learner.name,
                "Average": round(learner.get_average(), 2),
                "Category": learner.get_classification()
            })

        high_achiever_df = pd.DataFrame(high_achiever_data)

        print("\n")
        print("HIGH ACHIEVING LEARNERS".center(80))

        print(tabulate(high_achiever_df, headers="keys", tablefmt="psql", showindex=False))

    else:

        print("\n")
        print("HIGH ACHIEVING LEARNERS".center(80))
        print("No high achieving learners.")


    top_learner = get_top_learner(learner_list)

    top_data = [{
        "ID": top_learner.id_num,
        "Name": top_learner.name,
        "Average": round(top_learner.get_average(), 2)
    }]

    top_df = pd.DataFrame(top_data)


    # Display single top-performing learner in the Top Performing Learner Table using tabulate 
    print("\n")
    print("TOP PERFORMING LEARNER".center(80))

    print(tabulate(top_df,headers="keys", tablefmt="psql", showindex=False))

    print("=" * 80)



# Add learner and modules interactively with input validation & checking for prerequisites modules
def add_learner_interactive():

    print("\n--- ADD NEW LEARNER ---")

    # Get and validate learner ID
    while True:

        id_num = input("Enter Learner ID: ").strip()

        if  id_num == '':
            
            print("Learner ID cannot be empty.")
            
            continue

        # Check duplicate ID
        for learner in learners:

            if learner.id_num == id_num: 
                
                print("Learner ID already exists. Please enter a unique ID.")
                
                break

        else:

            break

    # Get and validate learner name
    while True:

        name = input("Enter Learner Name: ").strip()

        if name == '':
            print("Learner name cannot be empty.")
            continue

        break

    scores = []
    modules_done = []

    # Loop through modules to check prerequisites and get completion status and scores
    for module in modules:

        # Check if completed prerequisites for the module and print missing prerequisites if not completed
        if not prequisites_checking(module, modules_done):

            missing_modules = []

            # Check for missing prerequisites
            for prerequisite in prerequisite_facts.get(module, []):

                if prerequisite not in modules_done:

                    missing_modules.append(prerequisite)

                    print("Skipping " + module + ". Complete " + ", ".join(missing_modules) + " first.")
            
            continue

        # Check if learner completed the module
        while True:

            answer = input("Completed " + module + "? (y/n): ").strip().lower()

            if answer == 'y':
                modules_done.append(module)

                while True:

                    try:

                        score = float(input("Enter score for " + module + " (0-100): "))
                        if score >= 0 and score <= 100:

                            scores.append(score)
                            break

                        print("Score must be between 0 and 100.")

                    except ValueError:

                        print("Please enter a valid number.")

                break

            elif answer == 'n':

                break

            else:

                print("Please enter 'y' or 'n'.")

    # Try to create a Learner object and add it to the list
    try:

        learner = Learner(id_num, name, scores, modules_done)

        learners.append(learner)

        print("\nLearner " + name + " added successfully!")

    except ValueError as error:

        print("\n[Validation Failed]: " + error)


# Main program to display the dashboard and handle user input
def main():

    while True:
        display_dashboard(learners)

        print("\nOPTIONS:")
        print("1. Add Learner")
        print("2. Exit")

        choice = input("\nEnter choice (1-2): ").strip()

        if choice == "1":

            add_learner_interactive()

        elif choice == "2":

            print("\nExiting application. Goodbye!")

            break

        else:

            print("Invalid option. Please select 1 or 2.")


main()