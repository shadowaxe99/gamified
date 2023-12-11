```python
import pygame
from pygame import mixer

# Initialize Pygame Mixer for sound effects
mixer.init()

# SoundEffects class to manage and play sound effects for the gamified environment
class SoundEffects:
    def __init__(self):
        # Dictionary to store the sound effects
        self.effects = {
            'task_complete': mixer.Sound('sounds/task_complete.wav'),
            'new_badge': mixer.Sound('sounds/new_badge.wav'),
            'level_up': mixer.Sound('sounds/level_up.wav'),
            'achievement_unlocked': mixer.Sound('sounds/achievement_unlocked.wav'),
            'notification': mixer.Sound('sounds/notification.wav'),
            'click': mixer.Sound('sounds/click.wav'),
            'error': mixer.Sound('sounds/error.wav')
        }

    def play_effect(self, effect_name):
        """
        Play a sound effect based on the given effect name.
        
        :param effect_name: The name of the effect to play.
        """
        if effect_name in self.effects:
            self.effects[effect_name].play()
        else:
            print(f"Sound effect '{effect_name}' not found.")

# Example usage:
# sound_effects = SoundEffects()
# sound_effects.play_effect('task_complete')
```