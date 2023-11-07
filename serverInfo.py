import servers
from dateNtime import getDate, getTime
import json


server_info = [] 




def addServerInfo(host,check):
    template = {}
    global server_info
    curr_date = getDate()
    curr_time = getTime()
    template[host] = {"Status":check, "Date":curr_date, "Time":curr_time}
    server_info.append(template)#adds to template

def printServerInfo():
    for item in server_info:
        print(item)

def makeJsonServInfo():
    with open("servInfo.json", "w") as srvInfo:
        json.dump(server_info,srvInfo)

def getJsonServInfo():
    global server_info
    try:
        with open("servInfo.json", "r") as servInfoFile:
                server_info = json.load(servInfoFile)
    except:
        print("File doesn't exist/File not found")


#getJsonServInfo()

# for server in server_info:
#     for key, value in server.items():
#         print(f"Key {key}")
#         for inner_key, inner_value in value.items():
#             print(f"Inner key: {inner_key}, Inner value: {inner_value}")
        