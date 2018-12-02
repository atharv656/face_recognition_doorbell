import face_recognition
import cv2
import numpy as np
import pickle
import boto3
import time
from twilio.rest import Client

# sample pic of me TODO Change Face Encoding method: Identification faulty (racist)

def upload_to_database(item):
    dynamodb = boto3.resource('dynamodb',
                              aws_access_key_id='AKIAIIHNSC4U5PJUDVEQ',
                              aws_secret_access_key='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',
                              region_name='us-east-1')
    table = dynamodb.Table('smartlockfaces')
    with table.batch_writer() as batch:
        batch.put_item(Item={'time': int(time.time()), 'faces': item})


def box_faces(known_face_encodings=[], known_face_names=[]):
    """Displays the image of the given file with a green box around any detected faces
        Returns the locations of the faces like [ (top, right, bottom, left) ]"""
    video_capture = cv2.VideoCapture(0)
    while True:
        # Grab a single frame of video
        ret, frame = video_capture.read()

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_frame = frame[:, :, ::-1]

        # Find all the faces and face encodings in the frame of video
        face_locations = face_recognition.face_locations(rgb_frame)

        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        faces = []

        # Loop through each face in this frame of videoo
        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance=0.5)
            distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            name = "Unknown"

            # If a match was found in known_face_encodings, just use the first one.
            if True in matches:
                best_match = int(np.argmin([abs(x) for x in distances]))
                name = known_face_names[best_match]

            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
            faces.append(name)

        # Display the resulting image
        if len(face_locations) > 0:
            upload_to_database(str(faces))

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
            body=name,
            from_='+18303315151',
            to='+15184190103'
        )
    print(message.sid)

    # once stream is done
    video_capture.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    data = pickle.loads(open("encodings\encodings.pickle", "rb").read())
    # print(data)

    known_encodings = data["encodings"]

    known_names = data["names"]

    box_faces(known_encodings, known_names)