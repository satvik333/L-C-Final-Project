import json
from Game import Game
from TeamList import TeamList

def readJsonFile(filePath):
    try:
        file = open(filePath)
        fileData = json.loads(file.read())
        return fileData
    except:
        print('Error while reading a file')


def createTeam():
    # filePath = input("Enter the file path ")
    inputFileData = readJsonFile('C:/Users/satvik.ms/Desktop/final project diagrams/TeamsInputJSON.json')
    Game.gameType = inputFileData['gameType']
    playersDetails = inputFileData['players']
    noOfMembers = 0
    if (Game.gameType == 1):
        TeamList.total = int(len(playersDetails)/11)
        noOfMembers = 11
    elif (Game.gameType == 2):
        TeamList.total = int(len(playersDetails)/2)
        noOfMembers = 2
    else:
        TeamList.total = int(len(playersDetails))
        noOfMembers = 1
    playersList = []
    for i in range(TeamList.total):
        data = {
            "id": i + 1,
            "name": "Team - " + str(i),
            "gameType": Game.gameType,
            "players": playersDetails[0: noOfMembers]
        }
        playersList.append(data)
        del playersDetails[0: noOfMembers]
    TeamList.items = playersList
    teamData = {}
    teamData["teams"] = TeamList.items
    teamData["total"] = TeamList.total
    return teamData
    

print(createTeam())


