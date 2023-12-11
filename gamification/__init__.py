```python
from .points_system import PointsSystem
from .leaderboard import Leaderboard
from .challenge_mechanism import ChallengeMechanism
from .badge_system import BadgeSystem
from .profile_customization import ProfileCustomization
from .social_sharing import SocialSharing

# Initialize the gamification engine components
points_system = PointsSystem()
leaderboard = Leaderboard()
challenge_mechanism = ChallengeMechanism()
badge_system = BadgeSystem()
profile_customization = ProfileCustomization()
social_sharing = SocialSharing()

__all__ = [
    'points_system',
    'leaderboard',
    'challenge_mechanism',
    'badge_system',
    'profile_customization',
    'social_sharing'
]
```