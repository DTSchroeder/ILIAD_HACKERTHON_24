import pafy
import cv2
import torch

pafy.set_backend("yt-dlp")

# Replace with your livestream URL
url = 'https://www.youtube.com/watch?v=ssiZXK7mvJM'
video = pafy.new(url)
best = video.getbest(preftype="mp4")

# Open video stream with OpenCV
cap = cv2.VideoCapture(best.url)

# Process the livestream
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Stream ended or failed.")
        break

    # Apply YOLOv5 model to detect objects
    results = model(frame)

    # Render the results on the frame
    results.render()

    # Show the frame
    cv2.imshow('YOLO Object Detection on Livestream', frame)

    # Exit if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()