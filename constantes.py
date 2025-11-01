from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from drive_train import mt_crema, mt_cremaII

hub = PrimeHub()


def subirI():
    mt_crema.run_angle(1000, 180)
    #antihorario

def descerI():
    mt_crema.run_angle(1000,-180)
    #horario
