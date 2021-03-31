# ShotChartGenerator
Version 1.0

Using Python and the NBA API, one can create a shot chart with the matplotlib library

## Installing The NBA API

This python script makes use of the NBA Api which can be found here : https://pypi.org/project/nba-api/

To install the Python API a simple pip install is needed. Simply copy the following into your Python directory:

```bash
pip install nba-api
```

## Installing ShotChartGenerator

This script requires a few different libraries to work properly so make sure all the requirements are fulfilled by checking out the requirements.txt or doing

```bash
pip install -r requirements.txt
```

This script does all the parsing so all the user has to do is change the variable names to whatever player and year they want to take a look at.

## Example

The following code produces the subsequent chart.

```python
PLAYER_FIRST_NAME = 'Luka'
PLAYER_LAST_NAME = 'Doncic'
TEAM_NAME = 'Dallas Mavericks'
SEASON = '2018-19'
SEASON_TYPE = 'Regular Season'
CLR = 'blue'

Player = ShotChart(PLAYER_FIRST_NAME, PLAYER_LAST_NAME, TEAM_NAME, SEASON, SEASON_TYPE, CLR)
Player.main()
```

![Example](https://user-images.githubusercontent.com/74287805/113078970-04158b80-9189-11eb-83e1-fcf2711b5693.png)

If we change some of the variables, we can see how that changes the display,

```python
PLAYER_FIRST_NAME = 'Gordon'
PLAYER_LAST_NAME = 'Hayward'
TEAM_NAME = 'Boston Celtics'
SEASON = '2018-19'
SEASON_TYPE = 'Regular Season'
CLR = 'green'

Player = ShotChart(PLAYER_FIRST_NAME, PLAYER_LAST_NAME, TEAM_NAME, SEASON, SEASON_TYPE, CLR)
Player.main()
```

![Example](https://user-images.githubusercontent.com/74287805/113079231-81d99700-9189-11eb-9a1e-9e3f61792300.png)

## Changelog

### Version 1.0
- Release
