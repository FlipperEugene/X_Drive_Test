from vex import *

motor_1 = Motor(Ports.PORT11, GearSetting.RATIO_18_1, False)
motor_2 = Motor(Ports.PORT12, GearSetting.RATIO_18_1, False)
motor_3 = Motor(Ports.PORT14, GearSetting.RATIO_18_1, False)
motor_4 = Motor(Ports.PORT13, GearSetting.RATIO_18_1, False)

for motor in [motor_1, motor_2, motor_3, motor_4]:
    motor.spin(FORWARD)
    motor.set_velocity(100, PERCENT)
