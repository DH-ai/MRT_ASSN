#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import random




class daugher1(Node):
    def __init__(self):
        super().__init__("d_rover1")# type: ignore 
        self.publisher = self.create_publisher(Float32,"topic_1",10)
        time_period = 0.5 
        self.timer = self.create_timer(time_period,self.timer_callback)
    def timer_callback(self):
        msg = Float32()
        msg.data = float(random.randint(1,100))

        
        self.publisher.publish(msg)
        self.get_logger().info(str("Sent altitude data: "+str(msg._data)))
        


def main(args=None):
    rclpy.init(args=args)
    node = daugher1()
    # rclpy.create_node()
    rclpy.spin(node)
    rclpy.shutdown()