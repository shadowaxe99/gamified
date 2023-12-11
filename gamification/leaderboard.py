```python
import json
from operator import itemgetter

# Leaderboard class to manage the leaderboard entries
class Leaderboard:
    def __init__(self):
        # Initialize an empty list to store leaderboard entries
        self.entries = []

    def add_entry(self, user_id, points):
        """
        Add a new entry to the leaderboard or update an existing one.
        :param user_id: Unique identifier for the user.
        :param points: Points the user has earned.
        """
        # Check if the user already has an entry in the leaderboard
        existing_entry = next((entry for entry in self.entries if entry['user_id'] == user_id), None)
        if existing_entry:
            # Update the existing entry with the new points
            existing_entry['points'] += points
        else:
            # Create a new entry for the user
            self.entries.append({'user_id': user_id, 'points': points})
        # Sort the leaderboard entries based on points, descending
        self.entries.sort(key=itemgetter('points'), reverse=True)

    def get_leaderboard(self):
        """
        Retrieve the current leaderboard.
        :return: A JSON string representing the leaderboard.
        """
        return json.dumps(self.entries)

    def save_leaderboard(self, file_path):
        """
        Save the leaderboard to a file.
        :param file_path: Path to the file where the leaderboard will be saved.
        """
        with open(file_path, 'w') as file:
            json.dump(self.entries, file)

    def load_leaderboard(self, file_path):
        """
        Load the leaderboard from a file.
        :param file_path: Path to the file from which the leaderboard will be loaded.
        """
        with open(file_path, 'r') as file:
            self.entries = json.load(file)

    def reset_leaderboard(self):
        """
        Reset the leaderboard to an empty state.
        """
        self.entries = []

# Example usage:
# leaderboard = Leaderboard()
# leaderboard.add_entry('user123', 50)
# leaderboard.add_entry('user456', 75)
# leaderboard.add_entry('user123', 25)  # This will update the existing entry for 'user123'
# print(leaderboard.get_leaderboard())
# leaderboard.save_leaderboard('leaderboard.json')
# leaderboard.load_leaderboard('leaderboard.json')
# leaderboard.reset_leaderboard()
```