# This is an approximation of Python code

import time
from codrone_edu.drone import *

drone = Drone()
drone.pair()

minheight = None
maxheight = None
min_distance = None
max_distance = None

# goes to a place between two heights
def go_to_height(minheight, maxheight):
  global min_distance, max_distance
  while drone.get_height(unit="cm") >= maxheight:
    drone.go(0, 0, 0, -50, 0.5)
  while drone.get_height(unit="cm") <= minheight:
    drone.go(0, 0, 0, 100, 0.5)

# go to (min distance) (max distance). The distance will be
# between the two points would be the distance traversed
def go_to2(min_distance, max_distance):
  global minheight, maxheight
  while drone.get_pos_x("cm") >= max_distance:
    drone.go(0, -50, 0, 0, 0.5)
    print(drone.get_pos_x("cm"))
  while drone.get_pos_x("cm") <= min_distance:
    drone.go(0, 50, 0, 0, 0.5)
    print(drone.get_pos_x("cm"))


drone.takeoff()
go_to_height(100, 105)
go_to2(-100, -105)
drone.land()

drone.close()
