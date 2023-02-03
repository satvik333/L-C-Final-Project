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

def createFixtures(teamList, holidayList, Event):
    teams = teamList["teams"]
    matches = []
    for i in range(0, len(teams), 2):
        match = {
            "date": "20-03-2023 00:00:00",
            "teams": [teams[i]["name"], teams[i + 1]["name"]]
        }
        matches.append(match)
    output_data = {
        "gameId": 1,
        "matches": matches
    }
    print(output_data)
    return output_data


inputFileData = readJsonFile('C:/Users/satvik.ms/Desktop/final project diagrams/FixtureInputJSON.json')

teamList = inputFileData["listOfTeams"]
holidayList = inputFileData["holidayList"]
Event = inputFileData["event"]
createFixtures(teamList, holidayList, Event)