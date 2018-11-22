import face_recognition
import cv2

video_capture = cv2.VideoCapture(0)

# sample pic of me TODO Change Face Encoding method: Identification faulty (racist)
george_image = face_recognition.load_image_file("George.jpg")
george_face_encoding = face_recognition.face_encodings(george_image)[0]

john_image = face_recognition.load_image_file("john.jpg")
john_face_encoding = face_recognition.face_encodings(john_image)[0]


shaq_image = face_recognition.load_image_file("Shaq2.png")
shaq_face_encoding = face_recognition.face_encodings(shaq_image)[0]

trump_image = face_recognition.load_image_file("Donald_Trump.jpg")
trump_face_encoding = face_recognition.face_encodings(trump_image)[0]



# Create arrays of known face encodings and their names
known_face_encodings = [
    george_face_encoding,
    john_face_encoding,
    shaq_face_encoding,
    trump_face_encoding,

]
known_face_names = [
    "George Yin",
    "John Yin",
    "Shaq",
    "Donald Trump"
]

while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_frame = frame[:, :, ::-1]

    # Find all the faces and face enqcodings in the frame of video
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    # Loop through each face in this frame of video
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

        name = "Unknown"
        name_other= "Unknown"

        # If a match was found in known_face_encodings, just use the first one.
        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]
            second_match_index = matches.index(True)
            name_other = known_face_names[second_match_index]

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name_other, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# once stream is done
video_capture.release()
cv2.destroyAllWindows()
