import pafy
import cv2

# Replace with your livestream URL
url = 'https://www.youtube.com/watch?v=your_livestream_url'
video = pafy.new(url)
best = video.getbest(preftype="mp4")

# Open the video stream using OpenCV
cap = cv2.VideoCapture(best.url)