import json
from Event import Event
from FixtureList import FixtureList
from Ocassion import Occasion
import datetime
import random
import datetime

def generateDate(Event):
    eventStartDate = datetime.datetime.strptime(Event["startDate"], '%d-%m-%Y').date()
    eventEndDate = datetime.datetime.strptime(Event["endDate"], '%d-%m-%Y').date()
    start_date = datetime.date(int(eventStartDate.strftime('%Y')), int(eventStartDate.strftime('%m')), int(eventStartDate.strftime('%d')))
    end_date = datetime.date(int(eventEndDate.strftime('%Y')), int(eventEndDate.strftime('%m')), int(eventEndDate.strftime('%d')))
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    random_date = start_date + datetime.timedelta(days=random_days)
    normal_date_format = random_date.strftime('%d-%m-%Y')

    start_time = datetime.datetime.strptime("09:00:00", "%H:%M:%S").time()
    end_time = datetime.datetime.strptime("17:00:00", "%H:%M:%S").time()
    start_datetime = datetime.datetime.combine(datetime.datetime.today(), start_time)
    end_datetime = datetime.datetime.combine(datetime.datetime.today(), end_time)
    delta1 = end_datetime - start_datetime
    random_seconds = random.randint(0, int(delta1.total_seconds()))
    random_datetime = start_datetime + datetime.timedelta(seconds=random_seconds)
    random_time = random_datetime.time()
    
    return normal_date_format + ' ' + str(random_time)

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
            "date": generateDate(Event),
            "teams": [teams[i]["name"], teams[i + 1]["name"]]
        }
        matches.append(match)
    output_data = {
        "gameId": 1,
        "matches": matches
    }
    print(output_data)
    return output_data


inputFileData = readJsonFile('C:/Users/satvik.ms/Desktop/L-C-Final-Project/FixtureInput.json')

teamList = inputFileData["listOfTeams"]
holidayList = inputFileData["holidayList"]
Event = inputFileData["event"]
createFixtures(teamList, holidayList, Event)