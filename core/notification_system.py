```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Define the NotificationSystem class
class NotificationSystem:
    def __init__(self, email_server, email_port, email_user, email_password):
        self.email_server = email_server
        self.email_port = email_port
        self.email_user = email_user
        self.email_password = email_password

    def send_email(self, recipient, subject, body):
        """
        Send an email notification to a user.
        :param recipient: Email address of the recipient
        :param subject: Subject line of the email
        :param body: Body content of the email
        """
        message = MIMEMultipart()
        message['From'] = self.email_user
        message['To'] = recipient
        message['Subject'] = subject

        message.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP(self.email_server, self.email_port)
        server.starttls()
        server.login(self.email_user, self.email_password)
        text = message.as_string()
        server.sendmail(self.email_user, recipient, text)
        server.quit()

    def notify_task_completion(self, user_email, task_name):
        """
        Notify a user of task completion.
        :param user_email: Email address of the user
        :param task_name: Name of the completed task
        """
        subject = "Task Completed: {}".format(task_name)
        body = "Congratulations! You've completed the task: {}".format(task_name)
        self.send_email(user_email, subject, body)

    def notify_new_badge(self, user_email, badge_name):
        """
        Notify a user when they earn a new badge.
        :param user_email: Email address of the user
        :param badge_name: Name of the badge earned
        """
        subject = "New Badge Earned: {}".format(badge_name)
        body = "Great job! You've earned a new badge: {}".format(badge_name)
        self.send_email(user_email, subject, body)

    def notify_leaderboard_change(self, user_email, leaderboard_position):
        """
        Notify a user when their position on the leaderboard changes.
        :param user_email: Email address of the user
        :param leaderboard_position: New position on the leaderboard
        """
        subject = "Leaderboard Update"
        body = "Your new position on the leaderboard is: {}".format(leaderboard_position)
        self.send_email(user_email, subject, body)

# Example usage:
# notification_system = NotificationSystem('smtp.example.com', 587, 'your_email@example.com', 'your_password')
# notification_system.notify_task_completion('user_email@example.com', 'Design a new logo')
```