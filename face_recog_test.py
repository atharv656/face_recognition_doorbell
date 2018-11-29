import face_recognition
import cv2
import numpy as np


def show_image(image):
    """ displays a window with an image
        press any key to close the window"""
    cv2.namedWindow("output", cv2.WINDOW_NORMAL)
    cv2.imshow('output', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def box_faces(filename, known_face_encodings=[], known_face_names=[]):
    """Displays the image of the given file with a green box around any detected faces
        Returns the locations of the faces like [ (top, right, bottom, left) ]"""

    image = cv2.imread(filename)  # read the image

    face_locations = face_recognition.face_locations(image, number_of_times_to_upsample=3)
    # the location of the face in a list of tuples like [ (top, right, bottom, left) ]
    # if on a gpu computer, use model='cnn' parameter
    # number_of_times_to_upsample should be higher if there are small faces

    face_encodings = face_recognition.face_encodings(image, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        distances = face_recognition.face_distance(known_face_encodings, face_encoding)

        name = "Unknown"

        # If a match was found in known_face_encodings, just use the first one.
        if True in matches:
            best_match = np.argmin([abs(x) for x in distances])
            name = known_face_names[best_match]

        # Draw a box around the face
        cv2.rectangle(image, (left, top), (right, bottom), (0, 0, 255), 1)

        # set the scale of the font
        fontscale = np.prod(image.shape[:2]) / (1000 * 1000)

        # Draw a label with a name below the face
        cv2.rectangle(image, (left, bottom - int(40 * fontscale)), (right, bottom), (0, 0, 255), cv2.FILLED)

        font = cv2.FONT_HERSHEY_DUPLEX

        cv2.putText(image, name, (left + 6, bottom - 6), font, fontscale, (255, 255, 255), 1)

    show_image(image)
    return face_locations


if __name__ == '__main__':
    donald_image = face_recognition.load_image_file("Donald_Trump.jpg")
    donald_encoding = face_recognition.face_encodings(donald_image)[0]

    hillary_image = face_recognition.load_image_file("hillaryyoung.jpg")
    hillary_encoding = face_recognition.face_encodings(hillary_image)[0]

    bernie_image = face_recognition.load_image_file("bernieyoung.jpg")
    bernie_encoding = face_recognition.face_encodings(bernie_image)[0]
    known_encodings = [
        donald_encoding,
        hillary_encoding,
        bernie_encoding
    ]

    known_names = [
        "Donald Trump",
        "Hillary Clinton",
        "Bernie Sanders"
    ]

    box_faces("hillary-trump-bernie.jpg", known_face_encodings=known_encodings, known_face_names=known_names)
