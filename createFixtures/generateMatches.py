from generateFixturesDate import fixturedate

class match:
    def generate_match(teams, i, holidayList, Event, gameType):
        try:
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
        except Exception as e:
            print('Error while generating matches', e)