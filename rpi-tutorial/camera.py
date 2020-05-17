# camera.java

import picamera
import StringIO

def captureJPEG(width, height):
    '''
    Takes a camera picture with given picture size and returns the image
    in JPEG format. The picture resolution is width x height (max: 5 MPix)
    @param width: the width of the picture in pixels (max: 2592)
    @param height: the height of the picture in pixels (max: 1944)
    return: the image in JPEG format (as string); None, if the capture fails
    '''
    camera = picamera.PiCamera()
    imageData = StringIO.StringIO()
    w = int(width)
    h = int(height)

    try:
        camera.capture(imageData, format = "jpeg", resize = (w, h))
        imageData.seek(0)
        data = imageData.getvalue()
        return data
    finally:
        camera.close()
    return None  # error

def saveData(data, filename):
    '''
    Writes the given string data into a binary file.
    @param data: the data to store (as string type)
    @param filename: a valid filename in the local file space
    '''
    file = open(filename, "wb")
    file.write(data)
    file.close()

def captureAndSave(width, height, filename):
    '''
    Takes a camera picture with given picture size and stores is
    in JPEG format.
    The picture resolution is width x height (max: 5 MPix)
    @param width: the width of the picture in pixels (max: 2592)
    @param height: the height of the picture in pixels (max: 1944)
    @param filename: a valid filename in the local file space, 
    e.g. /home/pi/shot1.jpg
    '''
    data = captureJPEG(width, height)
    if data != None:
        saveData(data, filename)


