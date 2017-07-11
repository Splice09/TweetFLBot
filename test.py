#import player class
from Player import *


file = open("TweetID.txt", "r")

if file.mode == 'r':
    fileLines = file.readlines()
    PlayerList = [Player(line.split(",")[0], line.split(",")[1]) for line in fileLines]

file.close()

print(PlayerList[0].tsn)
print(PlayerList[0].tid)