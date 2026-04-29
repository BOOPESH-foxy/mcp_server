import threading

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
from fastmcp import FastMCP

# 2. THE ROS 2 NODE (The Listener)
class BatteryListener(Node):
    def __init__(self):
        super().__init__('mcp_battery_node')
        self.percentage = 0
        self.subscription = self.create_subscription(Int32, '/battery', self.listener_callback, 10)
        self.time_subscription = self.create_subscription(Int32, '/battery_estimation', self.estimation_callback, 10)

    def listener_callback(self, msg):
        self.percentage = msg.data
    
    def estimation_callback(self,msg):
        self.time = msg.data

rclpy.init()
node = BatteryListener()
threading.Thread(target=lambda: rclpy.spin(node), daemon=True).start()

mcp = FastMCP("RobotBattery")

@mcp.tool()
def get_live_battery():
    """Returns the real-time battery percentage from the /battery topic."""
    return f"Current Battery: {node.percentage}%"


@mcp.tool
def get_battery_estimation():
    "returns the estimation of battery life"
    return f"Estimation time for Battery: {node.time}mins"

if __name__ == "__main__":
    mcp.run()