from habit_tracker import HabitTracker

def main():

    """
    Main function to run the application.
    """

    tracker = HabitTracker()

    while True:
        print("\n--------------------------------")
        print("Welcome to the Habit Tracker!")
        print("--------------------------------")
        print("\n1. List all current habits")
        print("2. Add new habit")
        print("3. List all daily habits")
        print("4. List all weekly habits")
        print("5. List all longest streaks")
        print("6. Exit")
        
        choise = input("\nChoose an option to continue (1-6): ")

        if choise == "1":
            print("\n--------------------------------")
            tracker.list_all_habits()
            print("--------------------------------")
            choise = int(input(f"\nChoose a habit to perform some action (1-{len(tracker.habits)}): "))
            habit_name = tracker.habits[choise].name
            print("\n--------------------------------")
            action_choise = input(f"1. Complete habit {habit_name}\n2. Delete habit {habit_name}\n3. Show longest streak for {habit_name}\n--------------------------------\n\nChoose an option (1-3): ")

            if action_choise == "1":
                print("\n--------------------------------")
                tracker.complete_habit(choise)
                print("--------------------------------\n")
                break
            elif action_choise == "2":
                print("\n--------------------------------")
                tracker.delete_habit(choise)
                print("--------------------------------\n")
                break
            elif action_choise == "3":
                print("\n--------------------------------")
                tracker.get_streak(choise)
                print("--------------------------------\n")
                break
        elif choise == "2":
            name = input("Enter the name of the habit: ")
            periodicity = input("Enter the periodicity (daily or weekly): ")
            tracker.add_habit(name, periodicity)
            break
        elif choise == "3":
            print("\n--------------------------------")
            tracker.list_habits_by_periodicity("daily")
            print("--------------------------------\n")
            break
        elif choise == "4":
            print("\n--------------------------------")
            tracker.list_habits_by_periodicity("weekly")
            print("--------------------------------\n")
            break
        elif choise == "5":
            print("\n--------------------------------")
            tracker.list_longest_streaks()
            print("--------------------------------\n")
            break
        elif choise == "6":
            break
        
            
if __name__ == "__main__":
    main()