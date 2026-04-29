import rclpy
from rclpy.node import Node
from sensor_msgs.msg import BatteryState
from std_msgs.msg import String

class RobotBridge(Node):
    def __init__(self):
        super().__init__('antigravity_bridge')
        # Subscribing to your existing topics
        self.create_subscription(BatteryState, '/battery', self.battery_cb, 10)
        self.create_subscription(String, '/eta', self.eta_cb, 10)
        
        self.latest_data = {"battery": "Unknown", "eta": "Unknown"}

    def battery_cb(self, msg):
        self.latest_data["battery"] = f"{msg.percentage}%"

    def eta_cb(self, msg):
        self.latest_data["eta"] = msg.data

    def get_status(self):
        return self.latest_data

# Note: We will run this in a background thread in the MCP server