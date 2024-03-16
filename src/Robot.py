# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       BenWatford                                                   #
# 	Created:      3/13/2024, 9:55:11 AM                                        #
# 	Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *
import xDrive
import math


class Robot:
    def __init__(self, brain):
        self.brain = brain
        self.drivetrain = xDrive.Drive()

        self.drivetrain.calibrate()
        self.controller = Controller(PRIMARY)
        self.competition = Competition(self.user_control, self.pre_autonomous)
        self.setup_callbacks()
        self.user_control()

    def pre_autonomous(self):
        pass

    def user_control(self):
        self.brain.screen.print("Driver Control")

        while True:
            y = self.controller.axis4.position() / 100
            x = self.controller.axis3.position() / 100
            spin = (self.controller.axis1.position() / 100) * 0.75

            speed = math.sqrt(x ** 2 + y ** 2)
            angle = math.atan2(y, x)

            self.drivetrain.set_drive_speeds(angle, speed, spin)
            wait(10)

    def toggle_field_centric(self):
        self.drivetrain.toggle_field_centric()
        self.brain.screen.print("Toggling field centric, current state is: ")
        self.brain.screen.print(str(self.drivetrain.get_field_centric()))
        self.brain.screen.next_row()

    def setup_callbacks(self):
        self.controller.buttonA.pressed(self.toggle_field_centric)
