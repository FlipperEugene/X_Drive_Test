from vex import *
import Constants
import math


class Drive:
    def __init__(self):
        self.leftTop = Constants.motor_1  # Front Left
        self.rightTop = Constants.motor_2  # Front Right
        self.rightBottom = Constants.motor_3  # Back Right
        self.leftBottom = Constants.motor_4  # Back Left

        self.leftTop.spin(FORWARD)
        self.rightTop.spin(FORWARD)
        self.leftBottom.spin(FORWARD)
        self.rightBottom.spin(FORWARD)

        self.con = Constants.con

    @staticmethod
    def calculate_wheel_speed(wheel_direction,  move_direction, speed):
        return speed * math.cos(wheel_direction - move_direction)

    def set_drive_speeds(self,  direction,  speed,  spin):
        self.leftTop.set_velocity(self.calculate_wheel_speed(math.degrees(45), direction, speed) + spin,  PERCENT)
        self.rightTop.set_velocity(self.calculate_wheel_speed(math.degrees(-45), direction, speed) + spin,  PERCENT)
        self.leftBottom.set_velocity(self.calculate_wheel_speed(math.degrees(90+45), direction, speed) + spin,  PERCENT)
        self.rightBottom.set_velocity(self.calculate_wheel_speed(math.degrees(-90-45), direction, speed) + spin,  PERCENT)
