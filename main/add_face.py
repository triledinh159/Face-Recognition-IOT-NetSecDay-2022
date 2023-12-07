#from picamera import PiCamera
import argparse
import boto3
import time
import os
import cv2
import base64
#get args
parser = argparse.ArgumentParser(description='Capture image and add to collection.')
parser.add_argument('--collection', help='Collection Name', default='NetSecShow-faces')
parser.add_argument('--name', help='Face Name')
args = parser.parse_args()

message_bytes = args.name.encode('utf-8')
base64_bytes = base64.b64encode(message_bytes)
base64_message = base64_bytes.decode('utf-8')
base64_message = base64_message.replace('=', '')

#capture photo using pi camera
#camera = PiCamera()

#capture photo using camera module
camera = cv2.VideoCapture(0)
if camera.isOpened():
	retval, img = camera.read()


dirname = os.path.dirname(__file__)
directory = os.path.join(dirname, 'faces')
timestr = time.strftime("%Y%m%d-%H%M%S")
image = '{0}/image_{1}.jpg'.format(directory, timestr)
time.sleep(0.5)

cv2.imwrite(image,img) 

print ('Your image was saved to %s' % image)
#initialize reckognition sdk
client = boto3.client('rekognition')
with open(image, mode='rb') as file:
	response = client.index_faces(Image={'Bytes': file.read()}, CollectionId=args.collection, ExternalImageId=base64_message, DetectionAttributes=['ALL'])
print (response)
imgsrc = cv2.imread(image)
cv2.imshow('Stored', imgsrc)
cv2.waitKey(0)
cv2.destroyAllWindows()
