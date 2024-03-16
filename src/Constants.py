from vex import Ports, GearSetting


"""
    /--------\
    | 1    2     |
    |                |
    | 4    3     |
    \--------/ 
"""

"""Motor Init"""
drivetrain_gear_ratio = GearSetting.RATIO_18_1
drivetrain_inverted = False

front_left_motor_port = Ports.PORT11
front_right_motor_port = Ports.PORT12
back_left_motor_port = Ports.PORT14
back_right_motor_port = Ports.PORT13

inertial_port = Ports.PORT20

"""Class States"""


class debugState:
    On = 1
    Off = 2


class PrintState:
    Printed = 0
    NotPrinted = 1


class Field_Centric_State:
    Centric = 0
    NotCentric = 1
