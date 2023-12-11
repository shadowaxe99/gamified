```python
import requests
import json
from datetime import datetime

# Define the API keys and endpoints for the social media platforms
# These should be configured in a secure manner in production
SOCIAL_MEDIA_API_KEYS = {
    'twitter': 'YOUR_TWITTER_API_KEY',
    'facebook': 'YOUR_FACEBOOK_API_KEY',
    'instagram': 'YOUR_INSTAGRAM_API_KEY'
}

SOCIAL_MEDIA_ENDPOINTS = {
    'twitter': 'https://api.twitter.com/1.1/statuses/update.json',
    'facebook': 'https://graph.facebook.com/v9.0/me/feed',
    'instagram': 'https://graph.instagram.com/v1.0/media'
}

# Function to post a message to a specified social media platform
def post_to_social_media(platform, message):
    """
    Post a message to the specified social media platform.

    :param platform: The social media platform to post to ('twitter', 'facebook', 'instagram').
    :param message: The message to post.
    :return: Response from the social media API.
    """
    api_key = SOCIAL_MEDIA_API_KEYS.get(platform)
    endpoint = SOCIAL_MEDIA_ENDPOINTS.get(platform)
    
    if not api_key or not endpoint:
        raise ValueError(f"Invalid platform or API keys not configured for {platform}")

    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }

    data = {
        'message': message
    }

    response = requests.post(endpoint, headers=headers, data=json.dumps(data))
    return response.json()

# Function to schedule social media posts
def schedule_social_media_posts(posts_schedule):
    """
    Schedule social media posts based on the provided schedule.

    :param posts_schedule: A list of tuples containing the platform, message, and scheduled time.
    """
    for platform, message, schedule_time in posts_schedule:
        # Convert schedule_time to datetime object if it's a string
        if isinstance(schedule_time, str):
            schedule_time = datetime.strptime(schedule_time, '%Y-%m-%d %H:%M:%S')

        # Check if the scheduled time is in the future
        if schedule_time > datetime.now():
            # In a real-world scenario, we would use a task queue or scheduler like Celery
            # Here we just simulate the delay until the scheduled time
            delay_seconds = (schedule_time - datetime.now()).total_seconds()
            time.sleep(delay_seconds)
            post_to_social_media(platform, message)

# Example usage:
# posts_schedule = [
#     ('twitter', 'Check out our new gamified workflow automation tool!', '2023-04-01 12:00:00'),
#     ('facebook', 'Join the productivity revolution with our new app.', '2023-04-01 12:05:00'),
#     ('instagram', 'Boost your productivity with our gamified tool. #Productivity #Gamification', '2023-04-01 12:10:00')
# ]
# schedule_social_media_posts(posts_schedule)
```