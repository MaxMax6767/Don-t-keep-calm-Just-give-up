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

pygame.init()
mus = pygame.mixer.Sound("musique/music.mp3")
mus.set_volume(0.8)
mus.play(loops=-1, fade_ms=2000)


room1= game1()
while room1[0]!=True:
    room1=game1()

room2= game2()
while room2[0]!=True:
    room2=game2()

room3= game3()
while room3[0]!=True:
    room3=game3()

room4= game4()
while room4[0]!=True:
    room4=game4()

room5= game5()
while room5[0]!=True:
    room5=game5()

room6= game6()
while room6[0]!=True:
    room6=game6()

room7= game7()
while room7[0]!=True:
    room7=game7()

room8= game8()
while room8[0]!=True:
    room8=game8()

room9= game9()
while room9[0]!=True:
    room9=game9()

room10= game10()
while room10[0]!=True:
    room10=game10()

mus.stop()