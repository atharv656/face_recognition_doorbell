# face_recognition_doorbell

## Setup
We use the face_recognition python library.
[here](https://github.com/ageitgey/face_recognition) is its github
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

afterwards, maybe you can use pip, idk, but I cloned the [dlib repo](https://github.com/davisking/dlib) and opened it in cmd and ran
`python setup.py install --yes DLIB_USE_CUDA`

#### macOS, Ubuntu, or Raspbian (Raspberry Pi’s operating system)
Try to follow this [guide](https://www.pyimagesearch.com/2018/01/22/install-dlib-easy-complete-guide/)

## Things to do
Check out this [blog post](https://www.pyimagesearch.com/2018/06/18/face-recognition-with-opencv-python-and-deep-learning/)
. It shows how to do face recognition.

See how to do this recognition remotely or on the cloud.

add to this list if anything else is thought of.
