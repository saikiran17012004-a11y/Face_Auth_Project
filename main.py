import cv2
from deepface import DeepFace
import os

# 1. Initialize Camera
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret: break

    try:
        # 2. Compare live frame to the 'db' folder
        results = DeepFace.find(img_path=frame, 
                                db_path="db", 
                                model_name='Facenet', 
                                enforce_detection=False, 
                                silent=True)

        if len(results) > 0 and not results[0].empty:
            # 3. GET THE NAME: It takes the filename 'saikiran.jpg' and removes '.jpg'
            file_path = results[0]['identity'][0]
            identity_name = os.path.basename(file_path).split('.')[0].upper()
            
            # 4. Display your name on screen
            cv2.putText(frame, f"IDENTITY VERIFIED: {identity_name}", (30, 50), 
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        else:
            cv2.putText(frame, "UNKNOWN USER", (30, 50), 
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    except:
        pass

    cv2.imshow('Identity Check', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): break

cap.release()
cv2.destroyAllWindows()