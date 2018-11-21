import face_recognition
import cv2


def show_image(image):
    """ displays a window with an image
        press any key to close the window"""
    cv2.namedWindow("output", cv2.WINDOW_NORMAL)
    cv2.imshow('output', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def box_faces(filename, known_face_encodings, known_face_names):
    """Displays the image of the given file with a green box around any detected faces
        Returns the locations of the faces like [ (top, right, bottom, left) ]"""

    image = cv2.imread(filename)  # read the image

    face_locations = face_recognition.face_locations(image, number_of_times_to_upsample=1)
    # the location of the face in a list of tuples like [ (top, right, bottom, left) ]
    # if on a gpu computer, use model='cnn' parameter
    # number_of_times_to_upsample should be higher if there are small faces

    face_encodings = face_recognition.face_encodings(image, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

        name = "Unknown"

        # If a match was found in known_face_encodings, just use the first one.
        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]

        # Draw a box around the face
        cv2.rectangle(image, (left, top), (right, bottom), (0, 0, 255), 1)

        # Draw a label with a name below the face
        cv2.rectangle(image, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)

        font = cv2.FONT_HERSHEY_DUPLEX

        cv2.putText(image, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    show_image(image)
    return face_locations


if __name__ == '__main__':
    # picture of Trump
    trump_image = face_recognition.load_image_file("Donald_Trump.jpg")
    trump_face_encoding = face_recognition.face_encodings(trump_image)[0]
    known_face_encodings = [
        trump_face_encoding
    ]
    known_face_names = [
        "Donald Trump"
    ]

    box_faces("Donald_Trump.jpg", known_face_encodings, known_face_names)
