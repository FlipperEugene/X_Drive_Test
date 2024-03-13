from vex import Motor, Ports, GearSetting, Controller, Inertial, PRIMARY, Brain


con = Controller(PRIMARY)
"""
    /--------\
    | 1    2       |
    |                |
    | 3    4     |
    \--------/ 


"""
"""Motor Init"""
DriveTrainRatio = GearSetting.RATIO_18_1
motor_1 = Motor(Ports.PORT1, DriveTrainRatio, False)
motor_2 = Motor(Ports.PORT2, DriveTrainRatio, False)
motor_3 = Motor(Ports.PORT3, DriveTrainRatio, False)
motor_4 = Motor(Ports.PORT4, DriveTrainRatio, False)
inertial_21 = Inertial(Ports.PORT21)
brain = Brain()

"""Class States"""

class debugState:
    On = 1
    Off = 2

class PrintState:
    Printed = 1
    NotPrinted = 2

"""Print Function, Requesting "Text" which replaces the
existing brain.screen.print(""). If text was already called
then the function clears the screen."""

def print(Text):
    if PrintState == 2:
        brain.screen.print(Text)
        brain.screen.new_line
        PrintState.Printed
    elif PrintState == 1:
        brain.screen.clear_screen
        PrintState.NotPrinted