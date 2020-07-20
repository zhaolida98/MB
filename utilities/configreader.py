import configparser
import json


def readConfigData(section, key):
    config = configparser.ConfigParser()
    config.read('./ConfigFiles/Config.cfg')
    return config.get(section, key)


def fetchElementLocator(section, key):
    config = configparser.ConfigParser()
    config.read('./ConfigFiles/Element.cfg')
    return config.get(section, key)


def fetchElementData(section, key):
    config = configparser.ConfigParser()
    config.read('./ConfigFiles/data.cfg')
    return config.get(section, key)


try:
    with open('/Users/it000621/PycharmProjects/MB/configfile/Data.json') as Js:
        data = json.load(Js)
        user_data = data['UserData']
        url = data['Url']
        measure_data = data['MeasureData']
        value_set = data['Value-set']
        driver_path = data['driver_path']
        browser = data['browser']
except Exception as e:
    print(e)
