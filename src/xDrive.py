from vex import *
import Constants
import math


class Drive:
    def __init__(self):
        self.field_centric = False

        self.front_left = Motor(Constants.front_left_motor_port, Constants.drivetrain_gear_ratio, Constants.drivetrain_inverted)
        self.front_right = Motor(Constants.front_right_motor_port, Constants.drivetrain_gear_ratio, Constants.drivetrain_inverted)
        self.back_right = Motor(Constants.back_right_motor_port, Constants.drivetrain_gear_ratio, Constants.drivetrain_inverted)
        self.back_left = Motor(Constants.back_left_motor_port, Constants.drivetrain_gear_ratio, Constants.drivetrain_inverted)

        self.front_left.spin(FORWARD)
        self.front_right.spin(FORWARD)
        self.back_right.spin(FORWARD)
        self.back_left.spin(FORWARD)
        self.stop()

        self.inertial = Inertial(Constants.inertial_port)

    def calibrate(self):
        self.inertial.calibrate()
        while self.inertial.is_calibrating():
            wait(100, MSEC)

    @staticmethod
    def calculate_wheel_speed(wheel_direction, move_direction, speed):
        return speed * math.cos(wheel_direction - move_direction)

    @staticmethod
    def desaturate_wheel_velocities(wheel_speeds):
        max_wheel_velocity = max(wheel_speeds)
        if max_wheel_velocity > 1:
            for i in range(len(wheel_speeds)):
                wheel_speeds[i] = wheel_speeds[i] / max_wheel_velocity
        return wheel_speeds

    def set_drive_speeds(self, direction, speed, spin):

        if self.get_field_centric():
            direction -= math.radians(self.inertial.heading())

        front_left_wheel_speed = self.calculate_wheel_speed(math.radians(45), direction, speed) * math.sqrt(2) + spin
        front_right_wheel_speed = self.calculate_wheel_speed(math.radians(135), direction, speed) * math.sqrt(2) + spin
        back_left_wheel_speed = self.calculate_wheel_speed(math.radians(-45), direction, speed) * math.sqrt(2) + spin
        back_right_wheel_speed = self.calculate_wheel_speed(math.radians(-135), direction, speed) * math.sqrt(2) + spin

        (front_left_wheel_speed,
         front_right_wheel_speed,
         back_left_wheel_speed,
         back_right_wheel_speed) = self.desaturate_wheel_velocities([front_left_wheel_speed,
                                                                     front_right_wheel_speed,
                                                                     back_left_wheel_speed,
                                                                     back_right_wheel_speed])

        self.front_left.set_velocity(front_left_wheel_speed * 100, PERCENT)
        self.front_right.set_velocity(front_right_wheel_speed * 100, PERCENT)
        self.back_left.set_velocity(back_left_wheel_speed * 100, PERCENT)
        self.back_right.set_velocity(back_right_wheel_speed * 100, PERCENT)

    def stop(self):
        self.set_drive_speeds(0, 0, 0)

    def set_field_centric(self, field_centric):
        self.field_centric = field_centric

    def get_field_centric(self):
        return self.field_centric

    def toggle_field_centric(self):
        self.field_centric = not self.field_centric
        