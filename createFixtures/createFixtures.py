import json
from Event import Event
from FixtureList import FixtureList
from Ocassion import Occasion
import datetime


def readJsonFile(filePath):
    try:
        file = open(filePath)
        fileData = json.loads(file.read())
        return fileData
    except:
        print('Error while reading a file')

def createFixturesForBadminton(teamsDetails):
    pass

def createFixturesForCricket(teamsDetails):
    pass

def createFixturesForChess(teamsDetails):
    pass

def createFixtures(teamList, holidayList, event):
    teamsDetails = teamList["teams"]
    fixtureDetails = {}
    fixtureDetails["gameId"] = 1
    fixtureDetails["matches"] = []
    teamNames = []
    for team in teamsDetails:
        teamNames.append(team["name"])
    matchDetails = {}
    allMatchDetails = []
    for i in range(int(len(teamNames)/2)):
        matchDetails["date"] = datetime.datetime.now()
        matchDetails["teams"] = []
        teamOne = teamNames[0]
        teamTwo = teamNames[1]
        matchDetails["teams"].append(teamOne)
        matchDetails["teams"].append(teamTwo)
        del teamNames[0: 2]
        allMatchDetails.append(matchDetails)
    fixtureDetails["matches"].append(allMatchDetails)
    print(fixtureDetails)
    return fixtureDetails

inputFileData = readJsonFile('C:/Users/satvik.ms/Desktop/final project diagrams/FixtureInputJSON.json')

teamList = inputFileData["listOfTeams"]
holidayList = inputFileData["holidayList"]
event = inputFileData["event"]
createFixtures(teamList, holidayList, event)