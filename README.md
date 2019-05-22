## Face recognition doorbell
Smart Lock is a security system using facial recognition to identify potential threats and notify users rapidly.
[Devpost](https://devpost.com/software/smart-lock-ogu7zn)
## Motivation
Security systems for people nowadays are outdated. With SmartLock, face recognition can tell the difference between friendly faces and unknown people, alerting you when it matters.

## Screenshots
![](https://github.com/fidgetspinnerkid/face_recognition_doorbell/blob/master/screenshots/shaqscreenshot.PNG)
## Tech/framework used
- [dlib](https://github.com/davisking/dlib)
- [face_recognition](https://github.com/ageitgey/face_recognition)
- [twillio](https://www.twilio.com/)
- [OpenCV](https://opencv.org/)

## Installation
### Setup
We use the face_recognition python library.
[Here](https://github.com/ageitgey/face_recognition) is its github.
#### Windows
If you want to use your GPU with dlib then look below.

Easy download, type `pip install face_recognition` into the command prompt.

If you get a lot of errors, you need to download Visual Studio 2015 or 2017 and cmake.
Look online for Visual Studio and cmake. 
Make sure that when you install Visual Studio, you check the C++ options. 
Also make sure that you put Cmake into your path in environment variables.

Afterwards, you can try to download face_recognition using the pip command above.

##### With GPU
With a GPU, you should install Visual Studio 2015. Afterwards, install windows SDK 8.1, cmake, make sure you have cuda and cudnn installed(9.0 is ok), and also try to create a c++ project in visual studio to see if you can install the c++ option.

Clone the [dlib repo](https://github.com/davisking/dlib) and opened it in cmd and run
`python setup.py install --yes DLIB_USE_CUDA`

#### macOS, Ubuntu, or Raspbian (Raspberry Pi’s operating system)
Try to follow this [guide](https://www.pyimagesearch.com/2018/01/22/install-dlib-easy-complete-guide/)

## How to use?
If you have a webcam, run face_recog_live.py.
If not, then you can run face_recog_test.py and change the image file at the bottom.
### Encoding new faces
Add the pictures that you want to encode into the "dataset" folder under a folder of the name of the person in the image.
Then run in the command prompt in this directory:
`python encode_faces.py -i dataset -e encodings/encodings.pickle`
MIT © [fidgetspinnerkid](https://github.com/fidgetspinnerkid)
