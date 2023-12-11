```python
import json
from pathlib import Path

# Define the path to the user profile data file
USER_PROFILE_DATA_PATH = Path('data/user_profiles.json')

# Define the User class based on the shared user_profile_schema
class User:
    def __init__(self, user_id, username, avatar, badges, points):
        self.user_id = user_id
        self.username = username
        self.avatar = avatar
        self.badges = badges
        self.points = points

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'username': self.username,
            'avatar': self.avatar,
            'badges': self.badges,
            'points': self.points
        }

    @staticmethod
    def from_dict(data):
        return User(
            user_id=data['user_id'],
            username=data['username'],
            avatar=data['avatar'],
            badges=data['badges'],
            points=data['points']
        )

# ProfileCustomization class to handle user profile operations
class ProfileCustomization:
    def __init__(self):
        self.users = self.load_user_profiles()

    def load_user_profiles(self):
        try:
            with open(USER_PROFILE_DATA_PATH, 'r') as file:
                user_data = json.load(file)
                return {user['user_id']: User.from_dict(user) for user in user_data}
        except FileNotFoundError:
            return {}

    def save_user_profiles(self):
        with open(USER_PROFILE_DATA_PATH, 'w') as file:
            json.dump([user.to_dict() for user in self.users.values()], file, indent=4)

    def update_avatar(self, user_id, new_avatar):
        if user_id in self.users:
            self.users[user_id].avatar = new_avatar
            self.save_user_profiles()
            return True
        return False

    def add_badge(self, user_id, badge):
        if user_id in self.users:
            self.users[user_id].badges.append(badge)
            self.save_user_profiles()
            return True
        return False

    def update_username(self, user_id, new_username):
        if user_id in self.users:
            self.users[user_id].username = new_username
            self.save_user_profiles()
            return True
        return False

    def get_user_profile(self, user_id):
        return self.users.get(user_id)

# Example usage:
# profile_customization = ProfileCustomization()
# profile_customization.update_avatar('user123', 'new_avatar.png')
# profile_customization.add_badge('user123', 'Achievement Unlocked')
# profile_customization.update_username('user123', 'new_username')
```