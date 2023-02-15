import datetime
import random
from generateTime import generatetime
from generateScheduledDate import scheduleddate

class fixturedate:
    def generateDate(Event, holidayist):
        try:
            holidays = [i['date'] for i in holidayist]
            eventStartDate = datetime.datetime.strptime(Event["startDate"], '%d-%m-%Y').date()
            eventEndDate = datetime.datetime.strptime(Event["endDate"], '%d-%m-%Y').date()
            scheduledDate = scheduleddate.generateScheduledDate(eventStartDate, eventEndDate, holidays)
            random_time = generatetime.generateRandomTime()

            return scheduledDate + ' ' + str(random_time)
        except Exception as e:
            print('Error while generating date', e)