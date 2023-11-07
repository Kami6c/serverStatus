from dateNtime import getDate, getTime
import json


server_info = [] 



#Gets host and status from parameters aswell as date and time from other file and makes a dict then appends it to server_info
def addServerInfo(host,check):
    template = {}
    global server_info
    curr_date = getDate()
    curr_time = getTime()
    template[host] = {"Status":check, "Date":curr_date, "Time":curr_time}
    server_info.append(template)

#Test print not needed
def printServerInfo():
    for item in server_info:
        print(item)


#Makes json file from server_info
def makeJsonServInfo():
    with open("servInfo.json", "w") as srvInfo:
        json.dump(server_info,srvInfo)


#Gets json file from servInfo and assigns it to the server_info
def getJsonServInfo():
    global server_info
    try:
        with open("servInfo.json", "r") as servInfoFile:
                server_info = json.load(servInfoFile)
    except:
        print("File doesn't exist/File not found")

