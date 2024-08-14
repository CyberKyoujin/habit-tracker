import os
from habit import Habit

class HabitTracker:
    """
    A class to manage multiole habits.
    habits: {key(int): Habit(object of the class Habit)}
    """
    def __init__(self):
        self.habits = {}
        # loads existing habits from files.
        self.load_all_habits()

    def load_all_habits(self):
        """
        Loads predefined habits from 'habits' directory.
        """
        self.habits = {}
        i = 1
        for filename in os.listdir("habits"):
            if filename.endswith('.json'):
                name = filename[:-5]
                habit = Habit(name, "")
                habit.load_habit()
                self.habits[i] = habit
                i += 1

    def list_all_habits(self):
        """
        Prints all loaded habits and their details.
        """
        print("Your current habits:")
        for key, habit in self.habits.items():
            print(f"{key}. {habit.name}, {habit.periodicity}, current streak: {habit.get_streak()[0]} days/weeks.")

    def list_habits_by_periodicity(self, periodicity):
        """
        Filters habits by their periodicity (daily or weekly) and prints them.
        """
        filtered_habits = []
        for key, habit in self.habits.items():
            if habit.periodicity == periodicity:
                filtered_habits.append({key: habit})
        for habit_dict in filtered_habits:
            for key, habit in habit_dict.items():
                print(f"{key}. {habit.name}, {habit.periodicity}, current streak: {habit.get_streak()[0]} days/weeks.")
        return filtered_habits

    def add_habit(self, name, periodicity):
        """
        Adds a new habit to the tracker.
        """
        next_index = len(self.habits) + 1
        habit = Habit(name, periodicity)
        habit.save_habit()
        self.habits[next_index] = habit
        print(f"Habit '{name}' added.")

    def complete_habit(self, index):
        """
        Completes a habit by its index.
        """
        self.habits[index].complete_habit()

    def delete_habit(self, index, name=None):
        """
        Deletes a habit by its index.
        """
        if index in self.habits:
            habit = self.habits.pop(index)
            habit.delete_habit(name)

    def delete_habit_by_name(self, name):
        """
        Deletes a habit by its name.
        """
        keys = [key for key, habit in self.habits.items() if habit.name == name]
        for key in keys:
            self.delete_habit(key, name=name)

    def get_streak(self, index):
        """
        Displays the longest streak for a habit by index.
        """
        habit = self.habits[index]
        print(f"The longest streak for {habit.name} is {habit.get_streak()[1]}")

    def list_longest_streaks(self):
        """
        Lists all habits with longest streaks.
        """
        for key, habit in self.habits.items():
            print(f"{key}. {habit.name}, {habit.periodicity}, longest streak: {habit.get_streak()[1]} days/weeks.")