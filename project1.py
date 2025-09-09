import cv2
capture = cv2.VideoCapture(0)


face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

while True:
    success, img = capture.read()

    if not success:
        break

    faces = face_cascade.detectMultiScale(img, scaleFactor=1.2, minNeighbors=4)

    for (x, y, w, h) in faces:
        face_region = img[y:y+h, x:x+w]
        blurred_face = cv2.GaussianBlur(face_region, (151, 151), 0)
        img[y:y+h, x:x+w] = blurred_face

    if len(faces) == 0:
        cv2.putText(img, 'No Face Found!', (20, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)

   
    cv2.imshow('Face Blur', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


capture.release()
cv2.destroyAllWindows()

