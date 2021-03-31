from setup import *

# Variables To Change for Different Players and Years

PLAYER_FIRST_NAME = 'Gordon'
PLAYER_LAST_NAME = 'Hayward'
TEAM_NAME = 'Boston Celtics'
SEASON = '2018-19'
SEASON_TYPE = 'Regular Season'
CLR = 'green'

#Run This To Get Chart!

Player = ShotChart(PLAYER_FIRST_NAME, PLAYER_LAST_NAME, TEAM_NAME, SEASON, SEASON_TYPE, CLR)
Player.main()
