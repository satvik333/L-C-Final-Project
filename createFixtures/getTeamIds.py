import pyodbc

connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=ITT-SATVIK-MS;DATABASE=ISCdatabase;Trusted_Connection=yes;')
cursor = connection.cursor()

class teamids:
    def get_team_ids(teams, cursor):
            cursor.execute("SELECT * FROM Team WHERE Team.name IN ('{}')".format("', '".join(teams)))
            rst = cursor.fetchall()
            team_ids = []
            for team in rst:
                team_ids.append(team[0])
            return team_ids