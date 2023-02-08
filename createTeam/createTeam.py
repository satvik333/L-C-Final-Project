import json
from Game import Game
from TeamList import TeamList
import pyodbc

connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=ITT-SATVIK-MS;DATABASE=ISCdatabase;Trusted_Connection=yes;')
cursor=connection.cursor()

class readjson:
    def readJsonFile(filePath):
        try:
            file = open(filePath)
            fileData = json.loads(file.read())
            return fileData
        except Exception as e:
            print('Error while reading a file', e)
class saveplayers:
    def save_players_to_db(players, teamId):
        try:
            for player in players:
                cursor.execute("INSERT INTO Player(playerId,playerName) values (?, ?)", player['playerId'], player['name'])
                cursor.execute("INSERT INTO Team_Player(playerId, teamId) values (?, ?)", player['playerId'], teamId)
                cursor.commit()
        except Exception as e:
            print('Error in saving players of Team', e)

class saveteam:
    def save_team_to_db(teams):
        try:
            for team in teams:
                cursor.execute("INSERT INTO Team(teamId, name, eventId, gameId) values (?, ?, ?, ?)", team['id'], team['name'], 1, team["gameType"])
                saveplayers.save_players_to_db(team['players'], team['id'])
                cursor.commit()
        except Exception as e:
            print('Error in saving Team', e)


class getteam:
    def getTeams(gameId):
        try:
            cursor.execute("select * from Team, Player, Team_Player where Team.teamId = Team_Player.teamId AND Team_Player.playerId = player.playerId AND gameId = {}".format(gameId))
            result = cursor.fetchall()
            print("Teams are",result)
            return result
        except Exception as e:
            print('Error while retriving data', e)

class checkforgametype:
    def checkForGameTypeAndGetNoOfPlayers():
        options = {
            1: 11,
            2: 2
        }
        noOfMembers = options.get(Game.gameType, 1)
        try:
            TeamList.total = int(len(Game.players) / noOfMembers)
            if len(Game.players) < noOfMembers or len(Game.players) % noOfMembers != 0:
                raise ValueError('Cannot create teams')
        except ValueError as e:
            print(e)
        return noOfMembers

class readinputfile:
    def read_input_file():
        try:
            inputFileData = readjson.readJsonFile('C:/Users/satvik.ms/Desktop/L-C-Final-Project/TeamsInputJSON.json')
            return inputFileData
        except Exception as e:
            print('Error while reading input file:', e)
            return None

class gameTypeAndPlayers:
    def extract_game_type_and_players(inputFileData):
        Game.gameType = inputFileData['gameType']
        Game.players = inputFileData['players']

class numberOfPlayers:
    def get_number_of_players():
        noOfMembers = checkforgametype.checkForGameTypeAndGetNoOfPlayers()
        return noOfMembers

class teamList:
    def create_teams_list(noOfMembers):
        playersList = []
        for i in range(TeamList.total):
            data = {
                "id": i + 1,
                "name": "Team" + str(i),
                "gameType": Game.gameType,
                "players": Game.players[0: noOfMembers]
            }
            playersList.append(data)
            del Game.players[0: noOfMembers]
        TeamList.items = playersList
        return playersList

class jsonTeams:
    def create_teams_json(playersList):
        try:
            teamData = {}
            teamData["teams"] = playersList
            teamData["total"] = TeamList.total
            return json.dumps(teamData)
        except Exception as e:
            print('Error while creating teams json', e)

class createdTeams:
    def print_created_teams(teamsJson):
        try:
            print("Created Teams are", teamsJson)
        except Exception as e:
            print('Error while printing created teams:', e)

class createteams:
    def createTeams():
        try:
            inputFileData = readinputfile.read_input_file()
            gameTypeAndPlayers.extract_game_type_and_players(inputFileData)
            noOfMembers = numberOfPlayers.get_number_of_players()
            playersList = teamList.create_teams_list(noOfMembers)
            teamsJson = jsonTeams.create_teams_json(playersList)
            createdTeams.print_created_teams(teamsJson)
            saveteam.save_team_to_db(json.loads(teamsJson)['teams'])
            return teamsJson
        except Exception as e:
            print('Error while creating team', e)
   
    createTeams()
    # getteam.getTeams(2)


