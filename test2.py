#Create list of players to scrape tweets from
player_list = [line.rstrip('\n') for line in open("DauphinsTwitter.txt")]

for player in player_list:
    print player
