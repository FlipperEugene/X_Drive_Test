import math


class Units:
    inches_per_foot = 12.0
    meters_per_inch = 0.0254
    millimeters_per_centimeter = 100
    seconds_per_minute = 60
    milliseconds_per_second = 1000
    kilograms_per_pound = 0.453592

    def __init__(self):
        raise NotImplementedError("This is a utility class!")

    @staticmethod
    def meters_to_feet(meters):
        return Units.meters_to_inches(meters) / Units.inches_per_foot

    @staticmethod
    def feet_to_meters(feet):
        return Units.inches_to_meters(feet * Units.inches_per_foot)

    @staticmethod
    def meters_to_inches(meters):
        return meters / Units.meters_per_inch

    @staticmethod
    def inches_to_meters(inches):
        return inches * Units.meters_per_inch

    @staticmethod
    def centimeters_to_millimeters(centimeters):
        return centimeters * Units.millimeters_per_centimeter

    @staticmethod
    def millimeters_to_centimeters(millimeters):
        return millimeters / Units.millimeters_per_centimeter

    @staticmethod
    def degrees_to_radians(degrees):
        return math.radians(degrees)

    @staticmethod
    def radians_to_degrees(radians):
        return math.degrees(radians)

    @staticmethod
    def radians_to_rotations(radians):
        return radians / (math.pi * 2)

    @staticmethod
    def degrees_to_rotations(degrees):
        return degrees / 360

    @staticmethod
    def rotations_to_degrees(rotations):
        return rotations * 360

    @staticmethod
    def rotations_to_radians(rotations):
        return rotations * 2 * math.pi

    @staticmethod
    def rotations_per_minute_to_radians_per_second(rpm):
        return rpm * math.pi / (Units.seconds_per_minute / 2)

    @staticmethod
    def radians_per_second_to_rotations_per_minute(radians_per_second):
        return radians_per_second * (Units.seconds_per_minute / 2) / math.pi

    @staticmethod
    def milliseconds_to_seconds(milliseconds):
        return milliseconds / Units.milliseconds_per_second

    @staticmethod
    def seconds_to_milliseconds(seconds):
        return seconds * Units.milliseconds_per_second

    @staticmethod
    def kilograms_to_pounds(kilograms):
        return kilograms / Units.kilograms_per_pound

    @staticmethod
    def pounds_to_kilograms(lbs):
        return lbs * Units.kilograms_per_pound
