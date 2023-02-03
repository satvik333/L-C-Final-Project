import json
from Game import Game
from TeamList import TeamList
import pyodbc
connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=ITT-SATVIK-MS;DATABASE=ISCdatabase;Trusted_Connection=yes;')
cursor=connection.cursor()

def readJsonFile(filePath):
    try:
        file = open(filePath)
        fileData = json.loads(file.read())
        return fileData
    except:
        print('Error while reading a file')

def saveTeams(teams):
    for team in teams:
        cursor.execute("INSERT INTO Team(teamId, name, eventId, gameId) values (?, ?, ?, ?)", team['id'], team['name'], 1, team["gameType"])
        players = team['players']
        for player in players:
            cursor.execute("INSERT INTO Player(playerId,playerName) values (?, ?)", player['playerId'], player['name'])
            cursor.execute("INSERT INTO Team_Player(playerId, teamId) values (?, ?)", player['playerId'], team['id'])
        cursor.commit()


def getTeams(gameId):
    cursor.execute("select * from Team, Player, Team_Player where Team.teamId = Team_Player.teamId AND Team_Player.playerId = player.playerId AND gameId = {}".format(gameId))
    result = cursor.fetchall()
    return result


def createTeam():
    # filePath = input("Enter the file path ")
    inputFileData = readJsonFile('C:/Users/satvik.ms/Desktop/L-C-Final-Project/TeamsInputJSON.json')
    Game.gameType = inputFileData['gameType']
    Game.players = inputFileData['players']
    noOfMembers = 0
    if (Game.gameType == 1):
        TeamList.total = int(len(Game.players)/11)
        noOfMembers = 11
    elif (Game.gameType == 2):
        TeamList.total = int(len(Game.players)/2)
        noOfMembers = 2
    else:
        TeamList.total = int(len(Game.players))
        noOfMembers = 1
    playersList = []
    for i in range(TeamList.total):
        data = {
            "id": i + 1,
            "name": "Team - " + str(i),
            "gameType": Game.gameType,
            "players": Game.players[0: noOfMembers]
        }
        playersList.append(data)
        del Game.players[0: noOfMembers]
    TeamList.items = playersList
    teamData = {}
    teamData["teams"] = TeamList.items
    teamData["total"] = TeamList.total
    saveTeams(teamData["teams"])
    return json.dumps(teamData)
    
createTeam()
getTeams(2)


