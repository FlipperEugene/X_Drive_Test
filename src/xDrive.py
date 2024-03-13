from vex import *
import Constants
import math


class Drive:
    def __init__(self):
        self.con = None
        self.rightBottom = None
        self.leftBottom = None
        self.rightTop = None
        self.leftTop = None

    def init(self):
        Constants.print("Hello")
        self.leftTop = Constants.motor_1
        self.rightTop = Constants.motor_2
        self.leftBottom = Constants.motor_3
        self.rightBottom = Constants.motor_4
        self.con = Constants.con

    def set_drive_speeds(self, forward_speed, strafe_speed, turn_speed):
        motor_speed = math.sqrt(forward_speed ** 2 + strafe_speed ** 2 + turn_speed ** 2)
        angle = math.atan2(strafe_speed, forward_speed) + math.pi / 4

        left_top_speed = motor_speed * math.cos(angle)
        right_top_speed = motor_speed * math.sin(angle)
        left_bottom_speed = motor_speed * math.cos(angle + math.pi)
        right_bottom_speed = motor_speed * math.sin(angle + math.pi)

        self.leftTop.spin(FORWARD, abs(int(left_top_speed)))
        self.rightTop.spin(FORWARD, abs(int(right_top_speed)))
        self.leftBottom.spin(REVERSE, abs(int(left_bottom_speed)))
        self.rightBottom.spin(REVERSE, abs(int(right_bottom_speed)))
