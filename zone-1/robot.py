from sr.robot import *
import statistics
import math
from collections import defaultdict,deque

R = Robot()

m_left = R.motors[0].m0
m_right = R.motors[0].m1

def set_power(left, right):
    m_left.power = left
    m_right.power = right

def get_heading(n=5):
    heading = 0
    for i in range(0,n):
        heading += R.compass.get_heading()
    return heading/n * (360/math.tau)

def turn(degrees):
    radians = degrees * (math.tau/360))
    if radians != 0:
        per_tenth = 0.43737389828257306 
        sleep_time = math.fabs(radians)/per_tenth/10
        power = 75 
        p = math.copysign(power,radians)
    else:
        p = 0
    print(f"TURN power[{p}] sleep[{sleep_time}]")
    set_power(p,-p)
    R.sleep(sleep_time)

def move(power, distance):
    per_distance = 2
    sleep_time = math.fabs(distance/per_distance)
    p = math.copysign(power,distance)
    print(f"MOVE power[{p}] sleep[{sleep_time}]")
    set_power(p,p)
    R.sleep(sleep_time)

def stop(sleep_time=0.5):
    set_power(0,0)
    R.sleep(sleep_time)

# First part by dead-reckoning
move(75,1.4)
stop()
turn(40)
stop()
move(75,2.2)
stop(1.0)
R.radio.claim_territory()
move(100,2.6)
stop(1.5)
R.radio.claim_territory()
move(50,-2)
stop(1.5)