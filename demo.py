from room1_demo import *
from room2_demo import *

#demo for all people

room = game1()
while not room[0]:
    room = game1()

room2 = game2()
while not room2[0]:
    room2 = game2()

music("stop")
