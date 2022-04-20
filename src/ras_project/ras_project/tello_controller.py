import cv2 as cv
import numpy as np
import rclpy
from rclpy.time import Time
from rclpy.duration import Duration
from rclpy.node import Node
import sys
from sensor_msgs.msg import Image
from time import sleep
from std_msgs.msg import UInt8
from std_msgs.msg import Empty
from geometry_msgs.msg import Twist
from std_msgs.msg import Empty


class TelloController(Node):
    def __init__(self):
        super().__init__('image_listener')
        #self.cnt = 0
        self.image_counter = 0
        self.image_sub = self.create_subscription(Image, '/camera', self.image_sub_callback, 10)
        self.tello_pub = self.create_publisher(Twist, '/control', 10)
        #self.takeoff_pub = self.create_publisher(Empty, '/takeoff', 10)
        self.start = True
        self.detected_pub = self.create_publisher(UInt8, '/dance_moves', 10)
        self.jobdone_sub = self.create_subscription(UInt8, '/jobdone', self.jobdone_sub_callback, 10)
        self.detected_list = set()
        self.last_detected = 0
        self.waiting = False
        self.lined_up = False
        #self.takeoff_pub.publish(Empty())


    def image_sub_callback(self, msg):
        # test clock start
        # if self.clock_start is None:
        #     self.clock_start = self.get_clock().now()
        
        # clock_end = self.get_clock().now()
        # diff = clock_end - self.clock_start

        # if diff > Duration(seconds=3):
        #     print("hello world")
        #     self.clock_start = self.get_clock().now()
        
        # return None
        # test clock end

        self.image_counter += 1
        #print("Image received")

        # Convert ROS Image message to OpenCV2
        cv2_img = self.imgmsg_to_cv2(msg)
        cmdvel = Twist()

        if self.image_counter % 1 == 0:
            gray = cv.cvtColor(cv2_img, cv.COLOR_BGR2GRAY)

            arucoDict = cv.aruco.Dictionary_get(cv.aruco.DICT_4X4_100)
            arucoParams = cv.aruco.DetectorParameters_create()
            (corners, ids, rejected) = cv.aruco.detectMarkers(gray, arucoDict,
                parameters=arucoParams)
            
            if ids is not None:
                ids = ids[0]
                print("tag ids", ids)

            if self.waiting:
                cmdvel.linear.x = 0.0
                cmdvel.linear.z = 0.0
                cmdvel.linear.y = 0.0
                cmdvel.angular.z = 0.0
            elif ids is not None and len(ids) > 0 and not (ids[0] in self.detected_list): # and id not in list
                self.start = False
                

                # stop rotation
                cmdvel.angular.z = 0.0

                # send id to jetbot
                id_msg = UInt8()
                id_msg.data = int(ids[0])
                self.detected_pub.publish(id_msg)
                self.last_detected = ids[0]
                self.waiting = True

                # add id to list
                self.detected_list.add(ids[0])
                
            else:
                cmdvel.linear.x = 0.0
                cmdvel.linear.z = 0.0
                cmdvel.linear.y = 0.0
                cmdvel.angular.z = 0.0

                if self.start:
                    #print("start")
                    cmdvel.linear.z = 20.0
                else:
                    #print("rotate")
                    cmdvel.angular.z = 10.0
            
            #print(cmdvel)
            self.tello_pub.publish(cmdvel)
            #self.detected_pub.publish(msg)
            

    def jobdone_sub_callback(self, msg):
        if msg.data == self.last_detected:
            self.waiting = False

    
    def imgmsg_to_cv2(self, img_msg):
        n_channels = len(img_msg.data) // (img_msg.height * img_msg.width)
        dtype = np.uint8

        img_buf = np.asarray(img_msg.data, dtype=dtype) if isinstance(img_msg.data, list) else img_msg.data

        if n_channels == 1:
            cv2_img = np.ndarray(shape=(img_msg.height, img_msg.width),
                            dtype=dtype, buffer=img_buf)
        else:
            cv2_img = np.ndarray(shape=(img_msg.height, img_msg.width, n_channels),
                            dtype=dtype, buffer=img_buf)

        # If the byte order is different between the message and the system.
        if img_msg.is_bigendian == (sys.byteorder == 'little'):
            cv2_img = cv2_img.byteswap().newbyteorder()

        return cv2_img


def main():
    rclpy.init()
    tello_controller = TelloController()

    # Spin until ctrl + c
    rclpy.spin(tello_controller)

    tello_controller.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()