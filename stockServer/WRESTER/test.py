
import time
import json
textmessage = "training Started"
def handle_request():
    current_time = time.strftime("%H:%M:%S")
    response = {"message": "The current time is" + current_time}
    return response