from room7 import *
from room8 import *
from room9 import *
from room10 import *


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

music("stop")