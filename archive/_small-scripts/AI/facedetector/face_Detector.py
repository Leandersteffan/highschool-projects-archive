import cv2
from random import randrange

# Load trained data for frontal faces
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Choose something to detect a face
#img = cv2.imread('The_Rock_face.png')
#webcam = cv2.VideoCapture('Mein 2017   Felix von der Laden.mp4')
webcam = cv2.VideoCapture(0)

# Iterate over frames forever
while True:

    # Read current frame
    successful_frame_read, frame = webcam.read()

    # convert to grayscale
    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect Faces
    face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

    # draw rectangles around the faces
    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        #cv2.rectangle(frame, (x, y), (x + w, y + h), (randrange(256), randrange(256), randrange(256)), 2)


    cv2.imshow('Face Detector', frame)
    key = cv2.waitKey(1)

    #### Stop if Q key is pressed
    if key == 81 or key == 113:
        break

#### Release the VideoCapture object
webcam.release()

print('Code Completed')