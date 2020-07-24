import json


try:
    with open('/Users/it000621/PycharmProjects/MB/configfile/Data.json') as Js:
        data = json.load(Js)
        user_data = data['UserData']
        url = data['Url']
        measure_data = data['MeasureData']
        value_set = data['Value-set']
        driver_path = data['driver_path']
        browser = data['browser']
        title = data['Title']
except Exception as e:
    print(e)
