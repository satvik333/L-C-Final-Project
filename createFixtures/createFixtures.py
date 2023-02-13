import json
from Event import Event
from FixtureList import FixtureList
from Ocassion import Occasion
import datetime
import random
import datetime
import pyodbc

connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=ITT-SATVIK-MS;DATABASE=ISCdatabase;Trusted_Connection=yes;')
cursor = connection.cursor()

class fixturedate:
    def generateRandomTime():
        try:
            start_time = datetime.datetime.strptime("09:00:00", "%H:%M:%S").time()
            end_time = datetime.datetime.strptime("17:00:00", "%H:%M:%S").time()
            start_datetime = datetime.datetime.combine(datetime.datetime.today(), start_time)
            end_datetime = datetime.datetime.combine(datetime.datetime.today(), end_time)
            delta1 = end_datetime - start_datetime
            random_seconds = random.randint(0, int(delta1.total_seconds()))
            random_datetime = start_datetime + datetime.timedelta(seconds=random_seconds)
            return random_datetime.time()
        except Exception as e:
            print('Error while generating time', e)


    def isScheduledDateInHolidays(scheduledDate, holidays):
        return scheduledDate in holidays

    def generateScheduledDate(eventStartDate, eventEndDate, holidays):
        delta = eventEndDate - eventStartDate
        random_days = random.randint(0, delta.days)
        random_date = eventStartDate + datetime.timedelta(days=random_days)
        scheduledDate = random_date.strftime('%d-%m-%Y')
        maxDate = random_date.strftime('%Y-%m-%d')

        while fixturedate.isScheduledDateInHolidays(scheduledDate, holidays):
            scheduledDate = (datetime.datetime.strptime(scheduledDate, '%d-%m-%Y') + datetime.timedelta(days=1)).strftime('%d-%m-%Y')

        return scheduledDate

    def generateDate(Event, holidayist):
        try:
            holidays = [i['date'] for i in holidayist]
            eventStartDate = datetime.datetime.strptime(Event["startDate"], '%d-%m-%Y').date()
            eventEndDate = datetime.datetime.strptime(Event["endDate"], '%d-%m-%Y').date()
            scheduledDate = fixturedate.generateScheduledDate(eventStartDate, eventEndDate, holidays)
            random_time = fixturedate.generateRandomTime()

            return scheduledDate + ' ' + str(random_time)
        except Exception as e:
            print('Error while generating date', e)

class savefixture:
    def saveFixtures(matches):
        try:
            for match in matches:
                teams = match['teams']
                cursor.execute("SELECT * FROM Team WHERE Team.name IN ('{}')".format("', '".join(teams)))
                rst = cursor.fetchall()
                teamIds = []
                for team in rst:
                    teamIds.append(team[0])
                date_string = match['date']
                date_object = datetime.datetime.strptime(date_string, "%d-%m-%Y %H:%M:%S")
                date_string_sql = date_object.strftime("%Y-%m-%d %H:%M:%S")
                cursor.execute("INSERT INTO Matches(date, firstTeamId, secondTeamId, duration) values (?, ?, ?, ?)", date_string_sql,teamIds[0],teamIds[1],match['duration'] )
                cursor.commit()
        except Exception as e:
            print('Error while saving fixtures', e)

class readjson:
    def readJsonFile(filePath):
        try:
            file = open(filePath)
            fileData = json.loads(file.read())
            return fileData
        except Exception as e:
            print('Error while reading a file', e)


class FixtureList:
    matches = []

def generate_match(teams, i, holidayList, Event, gameType):
    duration = 0
    if (gameType == 2 or gameType == 3):
        duration = 30
    else:
        duration = 180
    return {
        "date": fixturedate.generateDate(Event, holidayList),
        "teams": [teams[i]["name"], teams[i + 1]["name"]],
        "duration": duration
    }
class createfixtures:
    def create_fixtures(teamList, holidayList, Event):
        try:
            teams = teamList["teams"]
            if (len(teams) % 2 != 0):
                return "Cannot create fixtures with odd number of teams"

            gameType = teams[0]['gameType']
            matches = [generate_match(teams, i, holidayList, Event, gameType) for i in range(0, len(teams), 2)]

            FixtureList.matches = matches
            # savefixture.saveFixtures(FixtureList.matches)

            output_data = {
                "gameId": gameType,
                "matches": matches,
            }
            print(output_data)
            return json.dumps(output_data)
        except Exception as e:
            print('Error while creating fixture', e)


inputFileData = readjson.readJsonFile('C:/Users/satvik.ms/Desktop/L-C-Final-Project/FixtureInput.json')
teamList = inputFileData["listOfTeams"]
holidayList = inputFileData["holidayList"]
Event = inputFileData["event"]
createfixtures.create_fixtures(teamList, holidayList, Event)