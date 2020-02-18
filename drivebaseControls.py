from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

import math
# Main code for drivebase controls
class drivebaseControls(object):

    def __init__(self, drivebase):
        self.drivebase = drivebase
        # Pull data from drivebase var for use in future 
        self.lMotor = self.drivebase.left_motor
        self.rMotor = self.drivebase.right_motor
        self.wheelCirc = self.drivebase.wheel_diameter * math.pi

    def Turn180(self):
        self.rMotor.reset_angle(0)
        self.drivebase.drive(0, 60)
        while self.rMotor.angle() > -555:
            pass
        self.drivebase.stop(Stop.BRAKE)
        wait(1000)

    def DriveDist(self, distance): # distance in mm
        self.lMotor.reset_angle(0)
        targetRots = distance / self.wheelCirc # number of rotations needed to reach target distance
        targetRots *= 360 # convert rotations to degrees
        if distance < 0:
            self.drivebase.drive(-100, 0)
            while self.lMotor.angle() > -1 * targetRots:
                pass
            self.drivebase.stop(Stop.BRAKE)
            wait(1000)
        else:
            self.drivebase.drive(100, 0)
            while self.lMotor.angle() < targetRots:
                pass
            self.drivebase.stop(Stop.BRAKE)
            wait(1000)

    """ Function specifically for subtask 1A"""
    def DriveDistRepeat(self, distance, forwardAngle, backwardAngle):
        if distance < 0:
            self.drivebase.drive(-100, 0)
            while self.lMotor.angle() > backwardAngle:
                pass
            self.drivebase.stop(Stop.BRAKE)
            wait(1000)
        else:
            self.drivebase.drive(100, 0)
            while self.lMotor.angle() < forwardAngle - 20:
                pass
            self.drivebase.stop(Stop.BRAKE)
            wait(1000)


