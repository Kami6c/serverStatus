import json
from ping import myping
from serverInfo import addServerInfo, getJsonServInfo, makeJsonServInfo, printServerInfo


servNames_to_scan = []


def getJson():
    global servNames_to_scan
    try:
        with open("serverNames.json", "r") as json_load:
            servNames_to_scan = json.load(json_load)
    except:
        print("File not found/File doesn't exists.")

# getJson()
# print(len(servNames_to_scan))
# for serv in servNames_to_scan:
#     print(serv)


def pingAllServs():
    getJson()
    for serv in servNames_to_scan:
        check = myping(serv)
        getJsonServInfo()
        addServerInfo(serv, check)
        makeJsonServInfo()
   
