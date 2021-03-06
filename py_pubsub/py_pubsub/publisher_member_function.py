# Copyright 2016 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class MinimalPublisher(Node):
    left_speed = 0
    right_speed = 0


    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher1_ = self.create_publisher(float, 'lspeed', 10)
        self.publisher2_ = self.create_publisher(float, 'rspeed', 10)
        
        timer_period = 0.1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg1 = float()
        msg2 = float()
        msg1.data = self.left_speed
        msg2.data = self.right_speed
        self.publisher1_.publish(msg1)
        self.publisher2_.publish(msg2)
        self.get_logger().info('Publishing: "%f" "%f"' % msg1.data, msg2.data)
        self.left_speed += 1
        self.right_speed += 1


def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
