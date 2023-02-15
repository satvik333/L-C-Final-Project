import pyodbc
from getTeamIds import teamids
from saveMatches import savematch

connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=ITT-SATVIK-MS;DATABASE=ISCdatabase;Trusted_Connection=yes;')
cursor = connection.cursor()

class savefixture:
    def save_fixtures(matches, cursor):
        try:
            for match in matches:
                savematch.save_match(match, cursor)
        except Exception as e:
            print('Error while saving fixtures', e)