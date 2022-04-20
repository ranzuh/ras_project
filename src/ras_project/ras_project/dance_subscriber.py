#from pickletools import uint8
import rclpy
from rclpy.node import Node

from std_msgs.msg import Uint8

from geometry_msgs.msg import Twist


class odomSubscriber(Node):
    def __init__(self):
        super().__init__("dance_subscriber")
        self.dance_counter = 0
        self.dance_subscription = self.create_subscription(
            Uint8, #Uint8
            '/dance_moves',
            self.dance_callback,
            10)
        self.dance_subscription
        self.publisherOutcome = self.create_publisher(Uint8, '/jobdone', 10)
        
        self.publisherCMD = self.create_publisher(Twist, '/cmd_vel', 10)
        


    def dance_callback(self, msg):
        #self.get_logger().info('I heard: "%s"' % msg.data)
        if(msg.data == 1):
            #turn left
            data = Twist()
            data.angular.z = 0.15
            self.publisherCMD.publish(data)
            self.publisherOutcome.publish(msg)
        elif(msg.data == 2):
            #turn right
            data = Twist()
            data.angular.z = -0.15
            self.publisherCMD.publish(data)
            self.publisherOutcome.publish(msg)
        elif(msg == 3):
            #idk, jump or sth
            data = Twist()
            data.angular.z = 0.5
            self.publisherCMD.publish(data)
            self.publisherOutcome.publish(msg)
        elif(msg == 4):
            #bury underground
            data = Twist()
            data.angular.z = 0.5
            self.publisherCMD.publish(data)
            self.publisherOutcome.publish(msg)


        
        self.publisher.publish()
        self.odom_counter += 1
        


    



def main():
    rclpy.init()
    dance_sub = odomSubscriber()
    
    # Spin until ctrl + c
    
    rclpy.spin(dance_sub)
    dance_sub.destroy_node()
    rclpy.shutdown()
    
if __name__ == '__main__':
    main()