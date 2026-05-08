import cv2
import os

# Create db folder if it doesn't exist
if not os.path.exists("db"):
    os.makedirs("db")

cap = cv2.VideoCapture(0)

print("--- Identity Enrollment ---")
print("Look at the camera and press 'S' to save your photo as 'saikiran'.")
print("Press 'Q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret: break

    # Mirror the frame for easier positioning
    display_frame = cv2.flip(frame, 1)
    
    cv2.putText(display_frame, "Press 'S' to Save", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    cv2.imshow('Enrollment - saikiran', display_frame)
    
    key = cv2.waitKey(1) & 0xFF
    if key == ord('s'):
        # Save the UNFLIPPED original frame for the AI
        photo_path = os.path.join("db", "saikiran.jpg")
        cv2.imwrite(photo_path, frame)
        print(f"SUCCESS: Saved to {photo_path}")
        break
    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()