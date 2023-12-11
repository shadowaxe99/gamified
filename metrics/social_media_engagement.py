```python
import json
from datetime import datetime
from core.notification_system import sendNotification

class SocialMediaEngagement:
    def __init__(self):
        self.engagement_data = []

    def record_engagement(self, user_id, platform, action, details):
        """
        Record a user's social media engagement activity.

        :param user_id: ID of the user
        :param platform: Social media platform on which the engagement occurred
        :param action: Type of engagement (like, share, comment, etc.)
        :param details: Additional details about the engagement
        """
        engagement = {
            'user_id': user_id,
            'platform': platform,
            'action': action,
            'details': details,
            'timestamp': datetime.now().isoformat()
        }
        self.engagement_data.append(engagement)
        self._save_engagement_data()
        sendNotification(user_id, SocialEngagementRecorded, "Your social engagement has been recorded.")

    def get_engagement_data(self):
        """
        Retrieve all recorded social media engagement data.

        :return: List of engagement records
        """
        return self.engagement_data

    def _save_engagement_data(self):
        """
        Save the engagement data to a file.
        """
        with open('data/social_engagement_data.json', 'w') as file:
            json.dump(self.engagement_data, file, indent=4)

# Constants for message names
SocialEngagementRecorded = 'SocialEngagementRecorded'

# Example usage
if __name__ == "__main__":
    social_media_engagement = SocialMediaEngagement()
    social_media_engagement.record_engagement(user_id='12345', platform='Twitter', action='tweet', details='Shared a new workflow!')
```