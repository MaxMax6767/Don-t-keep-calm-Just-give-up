from room1_demo import *
from room2_demo import *

room1= game1()
while room1[0]!=True:
    room1=game1()

room2= game2()
while room2[0]!=True:
    room2=game2()
