#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
from drivebaseControls import *


""" Variables to change based on subtask given values, edit as needed """
dist1A = 304.8 # distance for travel, in mm
n1A = 10 # number of steps to complete subtask a
dist1B = [100, 500, 300, 1] # distances to travel in order of occurance, add or remove list values as needed, in mm


""" Initialize drivebase variables """
leftDrive = Motor(Port.C, Direction.COUNTERCLOCKWISE) 
rightDrive = Motor(Port.B, Direction.COUNTERCLOCKWISE)
wheelDiameter = 75 # mm
axelLength = 130 # mm, distance between center of wheels


""" Initialize gyro sensor """
gyro = GyroSensor(Port.S1)


""" Initialize drivebase """
robot = DriveBase(leftDrive, rightDrive, wheelDiameter, axelLength)


""" Initialize drivebase controls """
driveControls = drivebaseControls(robot, gyro)


""" Subtask 1A """
def subtask1A(distance, n):

    # Set up continuous loop based on distance and number of steps
    sign = 1 # sign of direction for loop,
    forwardAng = (distance / driveControls.wheelCirc) * 360
    backwardAng = 0

    # Repeatedly drive n times for target distance
    for i in range(n):
        driveControls.DriveDistRepeat(dist1A * sign, forwardAng, backwardAng)
        sign *= -1


""" Subtask 1B """
def subtask1B(distance):

    # Based on distance array
    for dist in distance:

        # Go for specified distance, then turn around, repeat
        for i in range(2):
            driveControls.DriveDist(dist)
            driveControls.Turn180()
            

""" Reset motors """
leftDrive.reset_angle(0)
rightDrive.reset_angle(0)


""" Take input for which task to execute """
currTask = -1 # error subtask, should be either 1.1 or 1.2
brick.display.clear()
brick.display.text("L Button: Subtask 1A", (0, 50))
brick.display.text("R Button: Subtask 1B")
brick.display.text("M Button to Confirm")

# Keep scanning for input until center button is pressed
while not Button.CENTER in brick.buttons():
    if Button.LEFT in brick.buttons():
        currTask = 1.1
    if Button.RIGHT in brick.buttons():
        currTask = 1.2

# Based on button input, execute task
if currTask == 1.1:
    wait(1000) # add a short delay to program execute
    subtask1A(dist1A, n1A)
elif currTask == 1.2:
    wait(1000) # add a short delay to program execute
    subtask1B(dist1B)
else: # error, nothing executed
    brick.display.clear()
    brick.display.text("Error, no task selected.", (0, 50))
    brick.display.text("Rerun program.")
    wait(5000)











