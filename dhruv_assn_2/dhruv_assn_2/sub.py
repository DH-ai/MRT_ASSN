#! /usr/bin/env python3

import rclpy
from std_msgs.msg import Float32
from rclpy.node import Node

class subscribe(Node):
    def __init__(self):
        super().__init__("sub")# type: ignore 
        self.subscriber = self.create_subscription(Float32,"topic_1",self.timer_callback,10)
    def timer_callback(self,msg:Float32):
        self.get_logger().info("Recived"+str(msg))


def main (args = None):
    rclpy.init(args=args)
    node = subscribe()
    rclpy.spin(node)
    rclpy.shutdown()