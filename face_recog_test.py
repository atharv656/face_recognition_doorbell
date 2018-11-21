import face_recognition
import cv2


def show_image(image):
    cv2.namedWindow("output", cv2.WINDOW_NORMAL)
    cv2.imshow('output', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def box_faces(filename):
    """Displays the image of the given file with a green box around any detected faces
        Returns the locations of the faces like [ (top, right, bottom, left) ]"""

    image = cv2.imread(filename)

    face_locations = face_recognition.face_locations(image, number_of_times_to_upsample=3)
    # the location of the face in a list of tuples like [ (top, right, bottom, left) ]
    # if on a gpu computer, use model='cnn' parameter
    # number_of_times_to_upsample should be higher if there are small faces

    for (top, right, bottom, left) in face_locations:
        cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 1)  # draw a rectangle around the face

    show_image(image)
    return face_locations


if __name__ == '__main__':
    box_faces("John_Yin.jpg")

