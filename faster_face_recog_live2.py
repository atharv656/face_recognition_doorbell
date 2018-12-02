import face_recognition
import cv2
import pafy
from twilio.rest import Client
url = 'https://www.youtube.com/watch?v=niq1apTPdAE'
video = pafy.new(url)
best = video.getbest(preftype="mp4")
capture = cv2.VideoCapture()
capture.open(best.url)
#video_capture = cv2.VideoCapture(0)

# Load a sample picture and learn how to recognize it.
john_image = face_recognition.load_image_file("John.jpg")
john_face_encoding = face_recognition.face_encodings(john_image)[0]

# Create arrays of known face encodings and their names
known_face_encodings = [
    john_face_encoding,
]
known_face_names = [
    "John Yin",
]

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

while True:
    # Grab a single frame of video
    ret, frame = capture.read()

    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]

    # Only process every other frame of video to save time
    if process_this_frame:
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance=0.5)
            name = "Unknown"

            # If a match was found in known_face_encodings, just use the first one.
            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]

            face_names.append(name)

    process_this_frame = not process_this_frame


    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
if name == 'Unknown':
    # Your Account Sid and Auth Token from twilio.com/console
    account_sid = 'AC728087a5bdc48ee727ab84ed337833b0'
    auth_token = '3dfddade09d9aaae8c8bf4050f11a189'
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body='Stranger',
        from_='+18303315151',
        to='+15184190103'
    )
else:
    account_sid = 'AC728087a5bdc48ee727ab84ed337833b0'
    auth_token = '3dfddade09d9aaae8c8bf4050f11a189'
    client = Client(account_sid, auth_token)
    message = client.messages \
    .create(
        body='Friend',
        from_='+18303315151',
        to='+15184190103'
    )
print(message.sid)


# Release handle to the webcam
capture.release()
cv2.destroyAllWindows()
