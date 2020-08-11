import json
import os


try:
    with open('/Users/it000621/PycharmProjects/MB/Configs/Data.json') as Js:
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


try:
    with open("/Users/it000621/PycharmProjects/MB/Configs/Locators.json") as ls:
        Locators = json.load(ls)
        login= Locators['LoginPage']
        DSP = Locators['DataShopPage']
        MP = Locators['MeasurePage']
        VP = Locators['ValueSet']
except Exception as e:
    print(e)



try:
    with open("/Users/it000621/PycharmProjects/MB/Configs/database.json") as DB:
        database = json.load(DB)
        db = database['connectionString']

except Exception as e:
    print(e)






