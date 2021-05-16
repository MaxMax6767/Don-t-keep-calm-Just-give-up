#import all levels of the game
from room1 import *
from room2 import *
from room3 import *
from room4 import *
from room5 import *
from room6 import *
from room7 import *
from room8 import *
from room9 import *
from room10 import *

#launch first level, while player don't win this level, he can't pass to the second
room1 = game1()
while not room1[0]:
    room1 = game1()

#launch second level, while player don't win this level, he can't pass to the third
room2 = game2()
while not room2[0]:
    room2 = game2()

#launch level, while player don't win this level, he can't pass to the next
room3 = game3()
while not room3[0]:
    room3 = game3()

#launch level, while player don't win this level, he can't pass to the next
room4 = game4()
while not room4[0]:
    room4 = game4()

#launch level, while player don't win this level, he can't pass to the next
room5 = game5()
while not room5[0]:
    room5 = game5()

#launch level, while player don't win this level, he can't pass to the next
room6 = game6()
while not room6[0]:
    room6 = game6()

#launch level, while player don't win this level, he can't pass to the next
room7 = game7()
while not room7[0]:
    room7 = game7()

#launch level, while player don't win this level, he can't pass to the next
room8 = game8()
while not room8[0]:
    room8 = game8()

#launch level, while player don't win this level, he can't pass to the next
room9 = game9()
while not room9[0]:
    room9 = game9()

#launch level, while player don't win this level, he can't pass to the next
room10 = game10()
while not room10[0]:
    room10 = game10()

#stop music when player win the game
music("stop")
