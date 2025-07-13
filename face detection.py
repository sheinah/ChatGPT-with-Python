import cv2 # type: ignore

# Load pre-trained face detection model
face_cascade = cv2.CascadeClassifier('D:/programming/MyRepo/ChatGPT class/haarcascade_frontalface_default.xml')

# Read image from file
image = cv2.mired('D:/programming/MyRepo/ChatGPT class/Image.jpg')

# Resized_image
resized_img = cv2.resize(image, (400, 600))

# Convert image to grayscale
gray = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

# Draw rectangles around the detected faces
for (x, y, w, h) in faces:
    cv2.rectangle(resized_img, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Display the image with the detected faces
#cv2.imho('Image', resized_img)

# Wait for a key press and then close the window
cv2.imho('img', resized_img)
cv2.waitKey()
