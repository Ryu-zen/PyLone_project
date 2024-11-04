import json
import os
from datetime import datetime

# File to store habits data
DATA_FILE = 'habits.json'

# Load existing habits from the JSON file
def load_habits():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return {}

# Save habits to the JSON file
def save_habits(habits):
    with open(DATA_FILE, 'w') as file:
        json.dump(habits, file)

# Add a new habit
def add_habit(habits):
    habit = input("Enter the habit you want to track: ")
    habits[habit] = []
    save_habits(habits)
    print(f"Habit '{habit}' added!")

# Track completion of a habit
def complete_habit(habits):
    habit = input("Enter the habit you completed: ")
    if habit in habits:
        habits[habit].append(str(datetime.now()))
        save_habits(habits)
        print(f"Habit '{habit}' marked as completed!")
    else:
        print(f"Habit '{habit}' not found!")

# Display all habits and their completion status
def display_habits(habits):
    if not habits:
        print("No habits found.")
        return
    for habit, completions in habits.items():
        print(f"{habit}: {len(completions)} completed on {', '.join(completions)}")

# Main function to run the Habit Tracker
def main():
    habits = load_habits()
    while True:
        print("\nHabit Tracker")
        print("1. Add Habit")
        print("2. Complete Habit")
        print("3. Display Habits")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_habit(habits)
        elif choice == '2':
            complete_habit(habits)
        elif choice == '3':
            display_habits(habits)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()

