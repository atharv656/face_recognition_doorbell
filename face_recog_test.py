import face_recognition
import matplotlib.pyplot as plt
import matplotlib.patches as patches


fig, ax = plt.subplots(1)

image = face_recognition.load_image_file("OldPerson.jpg")

plt.imshow(image)

face_locations = face_recognition.face_locations(
    image)  # the location of the face in a list of tuples like [ (top, right, bottom, left) ]

for face in face_locations:
    x, y, width, height = (face[3],  # the x coord
                           face[2],  # the y coord
                           face[1] - face[3],  # the width
                           face[0] - face[2])  # the height

    rect = patches.Rectangle((x, y), width, height,
                             linewidth=1, edgecolor='r',
                             facecolor='none')  # draw a rectangle around the face
    ax.add_patch(rect)

plt.show()  # show the image with the rectangle
