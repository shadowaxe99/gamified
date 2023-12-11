```python
from .activity_tracker import ActivityTracker
from .conversion_rate_tracker import ConversionRateTracker
from .social_media_engagement import SocialMediaEngagementTracker
from .feedback_collection import FeedbackCollector

# Initialize the metrics module components
activity_tracker = ActivityTracker()
conversion_rate_tracker = ConversionRateTracker()
social_media_engagement_tracker = SocialMediaEngagementTracker()
feedback_collector = FeedbackCollector()

__all__ = [
    'activity_tracker',
    'conversion_rate_tracker',
    'social_media_engagement_tracker',
    'feedback_collector'
]
```