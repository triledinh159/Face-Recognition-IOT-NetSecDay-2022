# Face-Recognition-IOT-NetSecDay-2022

FRIOT v1.0

This project has been shown in NetSecDay 2022.

NetSec Day is the festival day of the Faculty of Computer Networks and Communications- University of Information Technology.

## Introduction
 - In this project, we have built a Face Recognition with an IOT system that not only can run on a PC but also run on an embedded computer (Raspberry Pi 3 in particular) at high performance while still ensuring accuracy.

 - To do that, we had to optimize the system. So, instead of full processing at the device, we will process the image on cloud services (AWS in this project).
 
## Procedures (updated!)
Before doing anything, please make sure that you have already installed python3, OpenCV, AWS SDK, and AWS CLI.
 
 - First, log in to your own AWS account on at local machine. Then, create a collection that will be used as a folder to store your data on AWS Rekognition.
```
     aws rekognition create-collection --collection-id "Your-collection"
```

 - Next, we need to add faces to our created collection. BTW, you also need to check the add_face.py in folder ./main/ . When everything is ok, let's upload faces.
```
    cd main
    python add_face.py --collection "Your-collection" --name "name"
```

 - At the recognition code, the device will make a pre-processing image which is captured before uploading to AWS to increase the accuracy.
```
    python face_recognition.py
```
 - We also use MQTT (IOT connection protocol) to transfer data after recognizing a face to other devices to store or use for the future.

![proc](/images/image.png "proc").
