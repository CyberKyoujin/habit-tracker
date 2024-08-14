import json
import os
from datetime import date, timedelta, datetime

os.makedirs("habits", exist_ok=True)

class Habit:

    """
    Main class representing a habit.
    Attributes: name - name of a habit.
                start_date - date when the habit was created.
                periodicity - daily or weekly.
                file_path - path to the JSON file where the habit data will be stored.
                completed - list of completion dates.
    """

    def __init__(self, name, periodicity):
        self.name = name
        self.start_date = date.today()
        self.periodicity = periodicity
        self.completed = []
        self.file_path = os.path.join("habits", f'{name}.json')

    def load_habit(self, file_path=None):
        """
        Loads habit data from a JSON file.
        """
        if file_path:
            self.file_path = file_path
        with open(self.file_path, 'r') as file:
            data = json.load(file)
            self.name = data['name']
            self.start_date = date.fromisoformat(data['start_date'])
            self.periodicity = data['periodicity']
            self.completed = data['completed']

    def save_habit(self):
        """
        Saves habit data to a JSON file.
        """
        data = {
            "name": self.name,
            "start_date": self.start_date.isoformat(),
            "periodicity": self.periodicity,
            "completed": self.completed
        }
        with open(self.file_path, 'w') as file:
            json.dump(data, file, indent=4)

    def complete_habit(self):
        """
        Appends the current date and time to completed array. 
        Checks whether the task was already completed today.
        """
        now = datetime.now()
        current_datetime = now.strftime('%Y-%m-%d %H:%M')
        completion_date = current_datetime.split(" ")[0]
        if any(completion_date in i for i in self.completed):
            print(f"The task '{self.name}' was already completed today!")
        else:
            self.completed.append(current_datetime)
            self.save_habit()
            print(f"Habit '{self.name}' was successfully completed at {current_datetime}.")

    def delete_habit(self, name=None):
        """
        Removes JSON file from the file system.
        """
        if name:
            path = os.path.join("habits", f'{name}.json')
            os.remove(path)
        else:
            os.remove(self.file_path)
            print(f"Habit '{self.name}' deleted.")

    def get_streak(self):
        """
        Calculates the longest and current streak of completions for habit in days or weeks.
        Returns 0, 0 if no completions have been made.
        """
        if not self.completed:
            return 0, 0

        completed_dates = sorted(date.fromisoformat(d.split(" ")[0]) for d in self.completed)
        longest_streak = 1
        current_streak = 1

        if self.periodicity == "daily":
            for i in range(len(completed_dates) - 1):
                if completed_dates[i + 1] - completed_dates[i] == timedelta(days=1):
                    current_streak += 1
                else:
                    longest_streak = max(longest_streak, current_streak)
                    current_streak = 1
            longest_streak = max(longest_streak, current_streak)

        elif self.periodicity == "weekly":
            # Getting the week number and year for the first date
            last_week = completed_dates[0].isocalendar()[1]
            last_year = completed_dates[0].isocalendar()[0]

            for i in range(1, len(completed_dates)):
                current_week = completed_dates[i].isocalendar()[1]
                current_year = completed_dates[i].isocalendar()[0]

                # Check if the current week is the next week
                if (current_year == last_year and current_week == last_week + 1) or \
                (current_year == last_year + 1 and last_week == 52 and current_week == 1):
                    current_streak += 1
                else:
                    longest_streak = max(longest_streak, current_streak)
                    current_streak = 1

                last_week = current_week
                last_year = current_year

            longest_streak = max(longest_streak, current_streak)

        return current_streak, longest_streak