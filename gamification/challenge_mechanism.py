```python
import random
from datetime import datetime, timedelta
from .points_system import PointsSystem
from .leaderboard import Leaderboard

class Challenge:
    def __init__(self, challenge_id, name, description, start_time, end_time, point_value):
        self.challenge_id = challenge_id
        self.name = name
        self.description = description
        self.start_time = start_time
        self.end_time = end_time
        self.point_value = point_value
        self.participants = set()
        self.completed_users = set()

    def add_participant(self, user_id):
        self.participants.add(user_id)

    def complete_challenge(self, user_id):
        if user_id in self.participants and user_id not in self.completed_users:
            self.completed_users.add(user_id)
            return True
        return False

    def is_active(self):
        return self.start_time <= datetime.now() <= self.end_time

    def get_point_value(self):
        return self.point_value

class ChallengeMechanism:
    def __init__(self):
        self.challenges = {}
        self.points_system = PointsSystem()
        self.leaderboard = Leaderboard()

    def create_challenge(self, name, description, duration_hours, point_value):
        challenge_id = self._generate_challenge_id()
        start_time = datetime.now()
        end_time = start_time + timedelta(hours=duration_hours)
        new_challenge = Challenge(challenge_id, name, description, start_time, end_time, point_value)
        self.challenges[challenge_id] = new_challenge
        return challenge_id

    def add_user_to_challenge(self, challenge_id, user_id):
        if challenge_id in self.challenges:
            challenge = self.challenges[challenge_id]
            if challenge.is_active():
                challenge.add_participant(user_id)

    def complete_challenge_for_user(self, challenge_id, user_id):
        if challenge_id in self.challenges:
            challenge = self.challenges[challenge_id]
            if challenge.complete_challenge(user_id):
                points_awarded = challenge.get_point_value()
                self.points_system.add_points(user_id, points_awarded)
                self.leaderboard.update_leaderboard(user_id, points_awarded)

    def _generate_challenge_id(self):
        return "CHL-" + str(random.randint(1000, 9999))

    def get_active_challenges(self):
        return {cid: ch for cid, ch in self.challenges.items() if ch.is_active()}

# Example usage:
# challenge_mechanism = ChallengeMechanism()
# challenge_id = challenge_mechanism.create_challenge("Code Sprint", "Complete the coding task in 2 hours.", 2, 100)
# challenge_mechanism.add_user_to_challenge(challenge_id, "user123")
# challenge_mechanism.complete_challenge_for_user(challenge_id, "user123")
```