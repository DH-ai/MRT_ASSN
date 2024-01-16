#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

import random
from geometry_msgs.msg import Point




class daugher2(Node):
    def __init__(self):
        super().__init__("d_rover2")# type: ignore 
        self.publisher = self.create_publisher(Point,"topic_2",10)
        time_period = 0.5
        self.timer = self.create_timer(time_period,self.timer_callback)
    def timer_callback(self):
        msg = Point()
        msg.x = float(random.randint(0,200))
        msg.y = float(random.randint(0,200))
        msg.z = 10.0
        String = f"Sent Location Data: X: {msg.x}, Y: {msg.y}, Z: {msg.z}"
        
        self.publisher.publish(msg)
        self.get_logger().info(String)
        


def main(args=None):
    rclpy.init(args=args)
    node = daugher2()
    # rclpy.create_node()
    rclpy.spin(node)
    rclpy.shutdown()