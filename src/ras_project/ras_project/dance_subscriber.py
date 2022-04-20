#from pickletools import uint8
import rclpy
from rclpy.node import Node

from std_msgs.msg import UInt8

from geometry_msgs.msg import Twist

import time


class DanceSubscriber(Node):
    def __init__(self):
        super().__init__("dance_subscriber")
        self.dance_counter = 0
        self.dance_subscription = self.create_subscription(
            UInt8, #Uint8
            '/dance_moves',
            self.dance_callback,
            10)
        self.dance_subscription
        self.publisherOutcome = self.create_publisher(UInt8, '/jobdone', 10)
        
        self.publisherCMD = self.create_publisher(Twist, '/cmd_vel', 10)
        


    def dance_callback(self, msg):
        #self.get_logger().info('I heard: "%s"' % msg.data)
        sleep_time = 5
        turn_vel = 0.5
        fwd_vel = 0.4
        print("got msg", msg.data)
        if(msg.data == 11):
            #turn left
            data = Twist()
            data.angular.z = turn_vel
            self.publisherCMD.publish(data)
            time.sleep(sleep_time)
            data.angular.z = 0.0
            self.publisherCMD.publish(data)

            self.publisherOutcome.publish(msg)
        elif(msg.data == 12):
            #turn right
            data = Twist()
            data.angular.z = -turn_vel
            self.publisherCMD.publish(data)
            time.sleep(sleep_time)
            data.angular.z = 0.0
            self.publisherCMD.publish(data)

            self.publisherOutcome.publish(msg)
        elif(msg.data == 13):
            #idk, jump or sth
            data = Twist()
            side = -1
            for i in range(4):
                side *= -1
                data.angular.z = side * turn_vel
                self.publisherCMD.publish(data)
                time.sleep(sleep_time/4)
                data.angular.z = 0.0
                self.publisherCMD.publish(data)
            
            self.publisherOutcome.publish(msg)
        elif(msg.data == 14):
            #bury underground
            data = Twist()
            side = -1
            for i in range(8):
                side *= -1
                data.linear.x = side * fwd_vel
                self.publisherCMD.publish(data)
                time.sleep(sleep_time/8)
                data.linear.x = 0.0
                self.publisherCMD.publish(data)

            self.publisherOutcome.publish(msg)
        


    



def main():
    rclpy.init()
    dance_sub = DanceSubscriber()
    
    # Spin until ctrl + c
    
    rclpy.spin(dance_sub)
    dance_sub.destroy_node()
    rclpy.shutdown()
    
if __name__ == '__main__':
    main()