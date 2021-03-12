#!/usr/bin/env python
import rospy
import cv2
import threading
from cv_bridge import *
from sensor_msgs.msg import Image
import string
import datetime

#Filename.avi
x = datetime.datetime.now()
date = x.strftime("%Y-%m-%d__%H:%M:%S")
form = ".avi"
record = date + form

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(record ,fourcc, 20.0, (640,480))

font = cv2.FONT_HERSHEY_TRIPLEX 

def image_callback(ros_image):
    global frame
    #cv_image = cv2.flip(cv2.flip(bridge.imgmsg_to_cv2(msg, desired_encoding = "passthrough"),0),1)
    cv_image = bridge.imgmsg_to_cv2(ros_image, desired_encoding = "bgr8")
    #*******************************************************
    cv_text = datetime.datetime.now()
    t = cv_text.strftime('%H:%M:%S')
    d = cv_text.strftime('%d/%m/%y')
    text = "Camera 1"
    image1 = cv2.putText(cv_image.copy(),t,(500,30), font, 1,(255,255,255),2)
    cv2.putText(image1,d,(0,30), font, 1,(255,255,255),2)
    cv2.putText(image1,text,(0,470), font, 1,(255,255,255),2)
    #*******************************************************
    cv_image = image1
    #cv_image = cv2.flip(image1,1)
    out.write(cv_image)
    frame = cv2.imencode(".jpeg",cv_image)[1].tobytes()
    event.set()
    
def node():
    rospy.init_node('image_converter', disable_signals=True)
    rospy.Subscriber("/camera_node/image_raw",Image, image_callback)

def returning():
    event.wait()
    #event.clear()
    return frame

def gen():
    while True:
        frame = returning()
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

def name():
    out.release()
    return record


#Start
bridge = CvBridge()
event = threading.Event()

init = threading.Thread(target=node)
ret = threading.Thread(target=returning)
init.start()
ret.start()
