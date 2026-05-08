import os
import base64
import cv2
import numpy as np
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from deepface import DeepFace
from datetime import datetime

# Initialize Flask and SocketIO
app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

# Create database folder if it doesn't exist
DB_PATH = "db"
if not os.path.exists(DB_PATH):
    os.makedirs(DB_PATH)

@app.route('/')
def index():
    """Render the main biometric dashboard."""
    return render_template('index.html')

@socketio.on('image')
def handle_image(data):
    """Process frames sent from the browser and run AI recognition."""
    try:
        # 1. Decode the Base64 image sent from the browser
        header, encoded = data.split(",", 1)
        data_decoded = base64.b64decode(encoded)
        nparr = np.frombuffer(data_decoded, np.uint8)
        frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        if frame is None:
            return

        # 2. AI Face Recognition Logic
        # We use 'Facenet' for high accuracy and 'cosine' for better light tolerance
        results = DeepFace.find(
            img_path=frame, 
            db_path=DB_PATH, 
            model_name='Facenet', 
            distance_metric='cosine',
            enforce_detection=False, 
            silent=True
        )

        # 3. Analyze Results
        if len(results) > 0 and not results[0].empty:
            # Get the top match path
            match_path = results[0]['identity'][0]
            # Extract the name from the filename (e.g., 'saikiran.jpg' -> 'saikiran')
            user_id = os.path.basename(match_path).split('.')[0].upper()
            
            # Log the successful entry to a CSV file
            with open("web_access_logs.csv", "a") as log_file:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                log_file.write(f"{timestamp},{user_id},Verified\n")
            
            # Send 'Verified' signal back to the browser
            emit('response', {'status': 'Verified', 'user': user_id})
        
        else:
            # Send 'Unknown' signal if no match is found
            emit('response', {'status': 'Unknown', 'user': 'None'})

    except Exception as e:
        # If the AI is warming up or a frame is blurry, send 'Searching'
        print(f"AI Processing Error: {e}")
        emit('response', {'status': 'Searching...', 'user': 'None'})

if __name__ == '__main__':
    # allow_unsafe_werkzeug=True is needed for running inside some local dev environments
    socketio.run(app, debug=True, port=5000)