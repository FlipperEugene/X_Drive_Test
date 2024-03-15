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
import Constants
import xDrive
import math


class Robot:
    def __init__(self, brain):
        self.brain = brain
        Constants.inertial_21.calibrate()
        self.brain.screen.print("INIT")
        self.con = Constants.con
        Constants.debugState = 1
        comp = Competition(self.user_control, self.pre_autonomous)
        self.user_control()

    def pre_autonomous(self):
        pass

    def user_control(self):
        self.brain.screen.print("Driver Control")
        drive = xDrive.Drive()

        while True:
            x = self.con.axis3.position()
            y = self.con.axis4.position()
            spin = self.con.axis1.position()

            speed = math.sqrt(x ** 2 + y ** 2)
            angle = math.atan2(y, x) - math.degrees(90)

            drive.set_drive_speeds(angle, speed, spin)
            wait(10)
