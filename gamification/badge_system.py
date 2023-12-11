```python
import json
from datetime import datetime

# Import shared dependencies
from .points_system import PointsSystem  # Assuming points_system.py is in the same gamification package

class Badge:
    def __init__(self, name, description, points_required):
        self.name = name
        self.description = description
        self.points_required = points_required
        self.created_at = datetime.now()

    def to_dict(self):
        return {
            'name': self.name,
            'description': self.description,
            'points_required': self.points_required,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S')
        }

class BadgeSystem:
    def __init__(self):
        self.badges = []
        self.user_badges = {}  # Maps user_id to a list of badge names

    def create_badge(self, name, description, points_required):
        badge = Badge(name, description, points_required)
        self.badges.append(badge)
        return badge

    def award_badge(self, user_id, badge_name):
        # Find the badge by name
        badge = next((b for b in self.badges if b.name == badge_name), None)
        if not badge:
            raise ValueError(f"Badge with name {badge_name} does not exist.")

        # Add the badge to the user's collection
        if user_id not in self.user_badges:
            self.user_badges[user_id] = []
        self.user_badges[user_id].append(badge_name)

        # Notify the user of the new badge
        self.notify_user_of_badge(user_id, badge)

    def notify_user_of_badge(self, user_id, badge):
        # Placeholder for notification logic
        # This would integrate with the notification_system module
        print(f"User {user_id} has been awarded a new badge: {badge.name}")

    def get_user_badges(self, user_id):
        return self.user_badges.get(user_id, [])

    def save_badges(self):
        with open('badges.json', 'w') as file:
            json.dump([badge.to_dict() for badge in self.badges], file, indent=4)

    def load_badges(self):
        try:
            with open('badges.json', 'r') as file:
                badges_data = json.load(file)
                self.badges = [Badge(**data) for data in badges_data]
        except FileNotFoundError:
            self.badges = []

# Example usage:
# badge_system = BadgeSystem()
# badge_system.create_badge("Task Master", "Complete 10 tasks", 100)
# badge_system.award_badge(user_id="user123", badge_name="Task Master")
# user_badges = badge_system.get_user_badges("user123")
# badge_system.save_badges()
# badge_system.load_badges()
```