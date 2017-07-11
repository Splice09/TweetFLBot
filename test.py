"""
Test script.
"""
#import player class
from Player import *


MY_FILE = open("TweetID.txt", "r")

if MY_FILE.mode == 'r':
    FILE_LINES = MY_FILE.readlines()
    PLAYER_LIST = [Player(line.split(",")[0], line.split(",")[1]) for line in FILE_LINES]

MY_FILE.close()

print PLAYER_LIST[0].tsn
print PLAYER_LIST[0].tid
