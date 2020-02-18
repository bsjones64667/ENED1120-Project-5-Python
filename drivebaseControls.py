from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

import math


""" Main code for drivebase controls """
class drivebaseControls(object):


    def __init__(self, drivebase): # TODO: Add gyro input once installed

        # Initialize drivebase for controls
        self.drivebase = drivebase

        # Pull data from drivebase var for use in future 
        self.lMotor = self.drivebase.left_motor
        self.rMotor = self.drivebase.right_motor
        self.wheelCirc = self.drivebase.wheel_diameter * math.pi


    """ Function to brake drive base for 1 second, written for repetitive use of code lines """
    def __BrakeStop(self):

        # Brake for 1 second
        self.drivebase.stop(Stop.BRAKE)
        wait(1000)


    """ Turn 180 based on motor angle 
        (will be replaced by gyro code, not consistent, based on friction of surface) """
    def Turn180(self):

        # Reset angle of rotation check motor
        self.rMotor.reset_angle(0)

        # Continue driving until angle has reached turn value
        self.drivebase.drive(0, 60)
        while self.rMotor.angle() > -555: # arbitrary value, not consistent
            pass

        # Brake
        self.__BrakeStop()
    

    """ New code for turn 180 once gyro is installed """
    """
    def Turn180(self)

        # Reset gyro angle to 0
        self.gyro.reset_angle(0)

        # Move until desired angle is reached
        self.drivebase.drive(0, 60)
        while self.gyro.angle() < 160: # A little under 180 as gyro measures angle late, mess with this value for consistency
            pass

        # Brake and 1 second delay to ensure stop
        self.__BrakeStop()
    """


    """ Drive a certain distance, based on rotations of the motor and circumference of wheel """
    def DriveDist(self, distance): # distance in mm

        # Reset distance motor angle
        self.lMotor.reset_angle(0)

        # Calculate target angle to rotate towards
        targetRots = distance / self.wheelCirc # number of rotations needed to reach target distance
        targetRots *= 360 # convert rotations to degrees

        # Move either forward or backwards based on distance sign until angle is reached
        if distance < 0:
            self.drivebase.drive(-100, 0)
            while self.lMotor.angle() > -1 * targetRots:
                pass
        else:
            self.drivebase.drive(100, 0)
            while self.lMotor.angle() < targetRots:
                pass

        # Brake
        self.__BrakeStop()


    """ Function specifically for subtask 1A, keeps original forward and backward positions 
        determined based on distance to travel """
    def DriveDistRepeat(self, distance, forwardAngle, backwardAngle):

        # Use forward and backward angles inputted and travel to those based on sign of distance
        if distance < 0:
            self.drivebase.drive(-100, 0)
            while self.lMotor.angle() > backwardAngle - 10: # subtract value to account for error
                pass
        else:
            self.drivebase.drive(100, 0)
            while self.lMotor.angle() < forwardAngle - 10: # subtract value to account for error
                pass

        # Brake
        self.__BrakeStop()
            


