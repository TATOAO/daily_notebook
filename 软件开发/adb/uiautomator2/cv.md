



# take screenshot and save to a file on the computer, require Android>=4.2.
d.screenshot("home.jpg")

# get PIL.Image formatted images. Naturally, you need pillow installed first
image = d.screenshot() # default format="pillow"
image.save("home.jpg") # or home.png. Currently, only png and jpg are supported

# get opencv formatted images. Naturally, you need numpy and cv2 installed first
import cv2
image = d.screenshot(format='opencv')
cv2.imwrite('home.jpg', image)

# get raw jpeg data
imagebin = d.screenshot(format='raw')
open("some.jpg", "wb").write(imagebin
