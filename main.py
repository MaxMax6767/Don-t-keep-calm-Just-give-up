from room1 import *
from room2 import *

room1= game1()
print("room1")
while room1[0]!=True:
    room1=game1()


room2= game2()
print("room2")
while room2[0]!=True:
    room2=game2()
