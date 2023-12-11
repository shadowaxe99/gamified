```python
import json
from flask import Flask, request, jsonify
from core.notification_system import sendNotification

app = Flask(__name__)

# Define the feedback form data schema
feedback_data_schema = {
    "type": "object",
    "properties": {
        "user_id": {"type": "string"},
        "feedback": {"type": "string"},
        "rating": {"type": "number"},
    },
    "required": ["user_id", "feedback", "rating"]
}

# Function to validate feedback data against the schema
def validate_feedback_data(data):
    try:
        jsonschema.validate(instance=data, schema=feedback_data_schema)
        return True
    except jsonschema.exceptions.ValidationError as err:
        return False

# Function to collect feedback from users
@app.route('/collect_feedback', methods=['POST'])
def collect_feedback():
    """
    Endpoint to collect feedback from users.
    Expects data in the format specified by feedback_data_schema.
    """
    feedback_data = request.get_json()
    if validate_feedback_data(feedback_data):
        # Process and store the feedback data
        # For demonstration purposes, we'll just print it
        print("Feedback collected:", feedback_data)
        # Send a notification to the user thanking them for their feedback
        sendNotification(feedback_data['user_id'], "Thank you for your feedback!")
        return jsonify({"message": "Feedback received successfully"}), 200
    else:
        return jsonify({"message": "Invalid feedback data"}), 400

if __name__ == '__main__':
    app.run(debug=True)
```