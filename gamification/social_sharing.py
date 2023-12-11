```python
import requests
from .points_system import calculatePoints
from .leaderboard import updateLeaderboard

# Define the SocialSharing class
class SocialSharing:
    def __init__(self, user_id, user_name, user_avatar):
        self.user_id = user_id
        self.user_name = user_name
        self.user_avatar = user_avatar

    # Function to share progress on social media
    def share_progress(self, platform, task_data):
        """
        Share user's progress on the specified social media platform.
        
        :param platform: str - Name of the social media platform
        :param task_data: dict - Data of the task to be shared
        """
        # Construct the message to be shared
        message = f"Hey everyone, I just completed a task and earned {calculatePoints(task_data)} points! Check out my progress on the leaderboard!"
        
        # Social media API endpoints (placeholders)
        api_endpoints = {
            'facebook': 'https://graph.facebook.com/v9.0/me/feed',
            'twitter': 'https://api.twitter.com/1.1/statuses/update.json',
            'instagram': 'https://api.instagram.com/v1/media',
            # Add other social media platform API endpoints here
        }
        
        # Check if the platform is supported
        if platform.lower() in api_endpoints:
            # Make a POST request to the platform's API to share the message
            response = requests.post(
                api_endpoints[platform.lower()],
                data={'message': message},
                headers={'Authorization': f'Bearer {self._get_access_token(platform)}'}
            )
            
            # Check if the post was successful
            if response.status_code == 200:
                print(f"Successfully shared on {platform}!")
                updateLeaderboard(self.user_id, calculatePoints(task_data))
            else:
                print(f"Failed to share on {platform}. Error: {response.text}")
        else:
            print(f"Platform {platform} is not supported for social sharing.")

    # Private function to get the access token for the social media API
    def _get_access_token(self, platform):
        """
        Retrieve the access token for the social media platform.
        
        :param platform: str - Name of the social media platform
        :return: str - Access token
        """
        # Placeholder for access token retrieval logic
        # In a real-world scenario, this would involve secure storage and retrieval of tokens
        return 'your_access_token_here'

# Example usage:
# user_social_sharing = SocialSharing(user_id='123', user_name='JaneDoe', user_avatar='avatar_url')
# user_social_sharing.share_progress(platform='facebook', task_data={'task_id': '456', 'points': 100})
```