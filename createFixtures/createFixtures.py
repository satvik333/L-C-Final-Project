import json
from Event import Event
from FixtureList import FixtureList
from Ocassion import Occasion

def readJsonFile(filePath):
    try:
        file = open(filePath)
        fileData = json.loads(file.read())
        return fileData
    except:
        print('Error while reading a file')

def createFixtures(teamList, holidayList, event):
    print('11111111', teamList)
    print('22222222222', holidayList)
    print('333333333', event)

inputFileData = readJsonFile('C:/Users/satvik.ms/Desktop/final project diagrams/TeamsInputJSON.json')
print('????????', inputFileData)