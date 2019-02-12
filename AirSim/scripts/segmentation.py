from sensor_msgs.msg import Image
from sensor_msgs.msg import CompressedImage
import rospy
import numpy as np
import airsim
import pprint
from cv_bridge import CvBridge


client = airsim.VehicleClient()
client.confirmConnection()

found = client.simSetSegmentationObjectID("Ball[\w]*", 22, True)
print("Found balls: %r" % (found))

found = client.simSetSegmentationObjectID("Cube[\w]*", 32, True)
print("Found balls: %r" % (found))

found = client.simSetSegmentationObjectID("Pyramid[\w]*", 42, True)
print("Found balls: %r" % (found))

found = client.simSetSegmentationObjectID("Sky[\w]*", 0, True)
print("Found sky: %r" % (found))

found = client.simSetSegmentationObjectID("Ground[\w]*", 1, True)
print("Found ground: %r" % (found))

responses = client.simGetImages([
    airsim.ImageRequest("0", airsim.ImageType.Segmentation, False, False)])
response = responses[0]
print("Type %d, size %d" % (response.image_type, len(response.image_data_uint8)))
img1d = np.fromstring(response.image_data_uint8, dtype=np.uint8)
img_rgba = img1d.reshape(response.height, response.width, 4)
img_rgba = np.flipud(img_rgba)
airsim.write_png('/sim/ml_scripts/images/segmentation.png', img_rgba)

