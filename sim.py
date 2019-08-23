from monopoly import *
from player import *

NUMPLAYERS = 4
players = []

# Create the set number of players
for x in range(NUMPLAYERS):
   players.append(Player(x,'ai'+str(x)))

# Create an instance of the game
mp=Monopoly(players)
mp.simGame()
