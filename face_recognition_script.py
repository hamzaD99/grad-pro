import face_recognition
import cv2
import numpy as np
import time
import telegram_sender
import os

video_capture = cv2.VideoCapture(0)
auth_driver = face_recognition.load_image_file("./Authorized Drivers/Hamza.jpeg")
auth_driver_face_encoding = face_recognition.face_encodings(auth_driver)[0]

auth_driver_2 = face_recognition.load_image_file("./Authorized Drivers/Big Boss.jpeg")
auth_driver_face_encoding_2 = face_recognition.face_encodings(auth_driver_2)[0]

known_face_encodings = [
    auth_driver_face_encoding,
    auth_driver_face_encoding_2
]
known_face_names = [
    "Hamza Maen",
    "Big Boss"
]
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True
start_time = time.time()
time_diff = 10

while True:
    ret, frame = video_capture.read()
    if process_this_frame:
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        rgb_small_frame = np.ascontiguousarray(small_frame[:, :, ::-1])
        
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

            face_names.append(name)
        valid = False
        for name in face_names:
            if not (name == 'Unknown'):
                valid = True
                break
        if valid:
            print("Welcome!")
            break
        else:
            current_time = time.time()
            diff = int(current_time - start_time)
            print(diff)
            if diff == time_diff:
                telegram_sender.sendMessage("Unauthorized Driver!")
                cv2.imwrite('temp.jpg',frame)
                telegram_sender.sendPhoto(open('temp.jpg','rb'))
                os.remove('temp.jpg')
                start_time = time.time()
    process_this_frame = not process_this_frame

    for (top, right, bottom, left), name in zip(face_locations, face_names):
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()