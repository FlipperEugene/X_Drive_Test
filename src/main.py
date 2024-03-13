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


class Robot:
    def __init__(self):
        self.con = None
        self.brain = None

    def init(self):
        self.brain = Brain()
        self.brain.screen.clear_screen()
        self.con = Constants.con
        Constants.debugState = 1
        comp = Competition(self.user_control, self.pre_autonomous)
        self.pre_autonomous()

    def pre_autonomous(self):
        pass

    def user_control(self):
        print("Driver Control")
        drive = xDrive.Drive()


        while True:
            forward_speed = self.con.axis3.position()
            strafe_speed = self.con.axis4.position()
            turn_speed = self.con.axis1.position()

            drive.set_drive_speeds(forward_speed, strafe_speed, turn_speed)
            wait(10)
