import json
from Event import Event
from generateMatches import match
from FixtureList import FixtureList
from readJsonFile import readjson
from saveFixtures import savefixture
from databaseConnection import database

cursor = database.connect_to_database()
class createfixtures:
    def create_fixtures(teamList, holidayList, Event):
        try:
            teams = teamList["teams"]
            if (len(teams) % 2 != 0):
                return "Cannot create fixtures with odd number of teams"

            gameType = teams[0]['gameType']
            matches = [match.generate_match(teams, i, holidayList, Event, gameType) for i in range(0, len(teams), 2)]

            FixtureList.matches = matches
            savefixture.save_fixtures(FixtureList.matches, cursor)

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