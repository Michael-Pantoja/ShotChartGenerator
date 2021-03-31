from nba_api.stats.endpoints import shotchartdetail
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np 
import requests
import json

class ShotChart:
    def __init__(self, FIRST_NAME, LAST_NAME, TEAM_NAME, SEASONYEAR, SEASON, COLOR):
        self.first = str(FIRST_NAME)
        self.color = COLOR
        self.metric = 'PTS'
        self.last = str(LAST_NAME)
        self.playerId = []
        self.team = str(TEAM_NAME)
        self.teamId = []
        self.JSON = []
        self.season = str(SEASONYEAR)
        self.type = str(SEASON)
        self.df = None
        self.teams = json.loads(requests.get('https://raw.githubusercontent.com/bttmly/nba/master/data/teams.json').text)
        self.players = json.loads(requests.get('https://raw.githubusercontent.com/bttmly/nba/master/data/players.json').text)
        self.initialized = False

        print('Initializing . . .')

    def main(self):
        while self.initialized == False:
            self.getInfo()
        self.getJSON()

    def getInfo(self):
        for team in self.teams:
            if team['teamName'] == self.team:
                self.teamId.append(team['teamId'])
        for player in self.players:
            if player['firstName'] == self.first and player['lastName'] == self.last:
                self.playerId.append(player['playerId'])
        self.initialized = True
        print('Getting PLayer and Team Info . . .')

    def getJSON(self):


        print('Gathering JSON . . .')
        playerJSON = shotchartdetail.ShotChartDetail(
            team_id = self.teamId,
            player_id = self.playerId,
            context_measure_simple = self.metric,
            season_nullable = self.season,
            season_type_all_star = self.type
        )

        playerData = json.loads(playerJSON.get_json())
        playerData = playerData['resultSets'][0]

        self.headers = playerData['headers']
        self.rows = playerData['rowSet']

        self.df = pd.DataFrame(self.rows)
        self.df.columns = self.headers

        self.chart()

    def chart(self):
        fig, ax = plt.subplots(1, 1, figsize = (8, 12))
        ax.plot([-220, -220], [0, 140], linewidth=2, color='Black')
        ax.plot([220, 220], [0, 140], linewidth=2, color='Black')
        ax.add_artist(mpl.patches.Arc((0, 140), 440, 315, theta1=0, theta2=180, facecolor='none', edgecolor='Black', lw=2))
        ax.plot([-80, -80], [0, 190], linewidth=2, color='Black')
        ax.plot([80, 80], [0, 190], linewidth=2, color='Black')
        ax.plot([-60, -60], [0, 190], linewidth=2, color='Black')
        ax.plot([60, 60], [0, 190], linewidth=2, color='Black')
        ax.plot([-80, 80], [190, 190], linewidth=2, color='Black')
        ax.add_artist(mpl.patches.Circle((0, 190), 60, facecolor='none', edgecolor='Black', lw=2))
        ax.add_artist(mpl.patches.Circle((0, 60), 15, facecolor='none', edgecolor='Black', lw=2))
        ax.scatter(self.df['LOC_X'], self.df['LOC_Y'] + 60, color = f'{self.color}', label = f"{self.first} {self.last} ({self.season})")
        ax.plot([-30, 30], [40, 40], linewidth=2, color='Black')
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_xlim(-250, 250)
        ax.set_ylim(0, 470)
        ax.legend()
        ax.set_title(f"{self.first} {self.last} Shooting Chart ({self.season})", size = 20)

        plt.savefig('Example')
        plt.show()
