import json

server_names = []

def appendToList(server):
    if server in server_names:
        print("Server already exists")
    else:
        server_names.append(server)

def printServer():
    if(len(server_names) == 0):
        print("Empty list")
    for item in server_names:
        print(item)
#Gets names from the jsonFile
def getJson():
    global server_names
    try:
        with open("serverNames.json", "r") as json_load:
            server_names = json.load(json_load)
    except:
        print("File not found/File doesn't exists.")

#Makes json file and puts server_names list in it
def makeJson():
    with open("serverNames.json", "w") as json_dump:
        json.dump(server_names, json_dump)

def deleteServ():
    serv_to_delete = input("Server name: ")
    if serv_to_delete in server_names:
        server_names.remove(serv_to_delete)
    else:
        print("No such server")