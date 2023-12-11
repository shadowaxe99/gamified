```python
class PointsSystem:
    """
    PointsSystem class to manage the point system for task completion and goal achievements.
    """
    def __init__(self):
        # Initialize a dictionary to keep track of user points
        self.user_points = {}

    def add_user(self, user_id):
        """
        Add a new user to the points system with a starting point of 0.
        :param user_id: Unique identifier for the user.
        """
        self.user_points[user_id] = 0

    def add_points(self, user_id, points):
        """
        Add points to a user's total points.
        :param user_id: Unique identifier for the user.
        :param points: Number of points to add.
        """
        if user_id in self.user_points:
            self.user_points[user_id] += points
        else:
            raise ValueError("User ID does not exist in the points system.")

    def subtract_points(self, user_id, points):
        """
        Subtract points from a user's total points.
        :param user_id: Unique identifier for the user.
        :param points: Number of points to subtract.
        """
        if user_id in self.user_points:
            self.user_points[user_id] -= points
        else:
            raise ValueError("User ID does not exist in the points system.")

    def get_points(self, user_id):
        """
        Get the total points for a user.
        :param user_id: Unique identifier for the user.
        :return: Total points of the user.
        """
        return self.user_points.get(user_id, 0)

    def reset_points(self, user_id):
        """
        Reset the points for a user to 0.
        :param user_id: Unique identifier for the user.
        """
        if user_id in self.user_points:
            self.user_points[user_id] = 0
        else:
            raise ValueError("User ID does not exist in the points system.")

# Example usage:
# points_system = PointsSystem()
# points_system.add_user("user123")
# points_system.add_points("user123", 10)
# current_points = points_system.get_points("user123")
# points_system.subtract_points("user123", 5)
# points_system.reset_points("user123")
```