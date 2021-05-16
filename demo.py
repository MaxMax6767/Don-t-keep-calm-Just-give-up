from room9 import *
from room10 import *

# Testing code launcher

room9 = game9()
while not room9[0]:
    room9 = game9()

room10 = game10()
while not room10[0]:
    room10 = game10()

music("stop")
