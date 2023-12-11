```python
import tkinter as tk
from tkinter import ttk

# Importing custom modules for interaction
from ui.gui_layout import renderGUI
from core.notification_system import sendNotification
from gamification.social_sharing import shareProgress

class Navigation:
    def __init__(self, root):
        self.root = root
        self.nav_frame = tk.Frame(self.root)
        self.nav_frame.pack(side=tk.TOP, fill=tk.X)

        # Navigation buttons
        self.home_button = ttk.Button(self.nav_frame, text="Home", command=self.go_home)
        self.profile_button = ttk.Button(self.nav_frame, text="Profile", command=self.go_profile)
        self.leaderboard_button = ttk.Button(self.nav_frame, text="Leaderboard", command=self.go_leaderboard)
        self.settings_button = ttk.Button(self.nav_frame, text="Settings", command=self.go_settings)
        self.share_button = ttk.Button(self.nav_frame, text="Share", command=self.go_share)

        # Place buttons on the navigation frame
        self.home_button.pack(side=tk.LEFT)
        self.profile_button.pack(side=tk.LEFT)
        self.leaderboard_button.pack(side=tk.LEFT)
        self.settings_button.pack(side=tk.LEFT)
        self.share_button.pack(side=tk.LEFT)

    def go_home(self):
        # Function to navigate to the home screen
        renderGUI(self.root, "home")
        sendNotification("Navigated to Home")

    def go_profile(self):
        # Function to navigate to the user profile
        renderGUI(self.root, "profile")
        sendNotification("Navigated to Profile")

    def go_leaderboard(self):
        # Function to navigate to the leaderboard
        renderGUI(self.root, "leaderboard")
        sendNotification("Navigated to Leaderboard")

    def go_settings(self):
        # Function to navigate to the settings page
        renderGUI(self.root, "settings")
        sendNotification("Navigated to Settings")

    def go_share(self):
        # Function to navigate to the share screen
        renderGUI(self.root, "share")
        shareProgress()
        sendNotification("Navigated to Share")

# Function to initialize navigation within the app
def setup_navigation(root):
    navigation = Navigation(root)
    return navigation

# Example usage:
# root = tk.Tk()
# navigation = setup_navigation(root)
# root.mainloop()
```