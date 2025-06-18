import cv2
# Use the correct path for the Haar cascade file
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# Try to open the IP camera stream
url = "http://100.100.56.170:8080/video"
video_cap = cv2.VideoCapture(url)

if not video_cap.isOpened():
    print(f"Failed to open stream at {url}. Trying local webcam...")
    video_cap = cv2.VideoCapture(0)
    if not video_cap.isOpened():
        print("Failed to open local webcam. Please check your camera connection.")
        exit(1)
    else:
        print("Local webcam opened successfully.")
else:
    print(f"Stream opened successfully at {url}")

while True:
    ret, video_data = video_cap.read()
    if not ret or video_data is None:
        print("Failed to grab frame from camera. Check if the stream URL is correct and accessible.")
        break
    col = cv2.cvtColor(video_data, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        col,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    for (x, y, w, h) in faces:
        cv2.rectangle(video_data, (x, y), (x + w, y + h), (255, 0, 0), 2)
    cv2.imshow("Video_live", video_data)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
video_cap.release()
cv2.destroyAllWindows()
