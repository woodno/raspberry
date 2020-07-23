# Camera1.py

import camera

print "Capturing image..."
img = camera.captureJPEG(300, 200)
print "size", len(img)
camera.saveData(img, "/home/pi/test.jpg")
print "JPEG saved"
