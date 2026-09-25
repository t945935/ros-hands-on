import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class Listener(Node):
    """Print messages received on the generic /chatter topic."""

    def __init__(self):
        super().__init__('listener')
        self.subscription = self.create_subscription(
            String, 'chatter', self.on_message, 10
        )

    def on_message(self, message):
        self.get_logger().info(f'Received: {message.data}')


def main(args=None):
    rclpy.init(args=args)
    node = Listener()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
