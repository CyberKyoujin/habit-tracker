import unittest
import os
import json
from habit_tracker import HabitTracker
from datetime import datetime

class TestHabitTracker(unittest.TestCase):

    """
    Testing class for HabitTracker
    """
    
    def setUp(self):
        # Creating instance of HabitTracker.
        self.tracker = HabitTracker()
        
    def tearDown(self):
        # Deleting test file after tests.
        self.tracker.delete_habit_by_name("Yoga")

    def test_load_all_habits(self):
        self.tracker.load_all_habits()
        self.assertEqual(len(self.tracker.habits), 5)

    def test_list_habits_by_periodicity(self):
        self.tracker.load_all_habits()
        daily_habits = self.tracker.list_habits_by_periodicity("daily")
        weekly_habits = self.tracker.list_habits_by_periodicity("weekly")
        self.assertEqual(len(daily_habits), 3)
        self.assertEqual(len(weekly_habits), 2)
    
    def test_add_habit(self):
        self.tracker.load_all_habits()
        self.tracker.add_habit("Yoga", "daily")
        self.assertEqual(len(self.tracker.habits), 6)
    
    def test_complete_habit(self):
        self.tracker.load_all_habits()
        habit = self.tracker.habits[2]
        habit.complete_habit()
        self.assertIn(datetime.now().strftime('%Y-%m-%d %H:%M'), habit.completed)

    def test_delete_habit(self):
        self.tracker.load_all_habits()
        self.tracker.delete_habit_by_name("Yoga")
        self.assertNotIn("Yoga", [h.name for h in self.tracker.habits.values()])

    def test_get_streak(self):
        self.tracker.load_all_habits()
        habit = self.tracker.habits[1]
        streak = habit.get_streak()[0]
        self.assertGreaterEqual(streak, 0)
            
if __name__ == "__main__":
    unittest.main()