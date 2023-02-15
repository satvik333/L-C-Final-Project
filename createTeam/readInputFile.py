from readJson import readjson

class readinputfile:
    def read_input_file():
        try:
            inputFileData = readjson.readJsonFile('C:/Users/satvik.ms/Desktop/L-C-Final-Project/TeamsInputJSON.json')
            return inputFileData
        except Exception as e:
            print('Error while reading input file:', e)
            return None