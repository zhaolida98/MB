import json

try:
    with open('./configfile/Data.json') as Js:
        data = json.load(Js)
        user_data = data['UserData']
        url = data['Url']
        measure_data = data['MeasureData']
except Exception as e:
    print(e)
