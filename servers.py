import json

server_names = []

#Adds server to the list
def appendToList(server):
    if server in server_names:
        print("Server already exists")
    else:
        server_names.append(server)
#Test print not needed
def printServer():
    if(len(server_names) == 0):
        print("Empty list")
    for item in server_names:
        print(item)

#Gets names from the serverNames.json and puts it inside server_names global needs to be there otherwise it will create inside the scope
def getJson():
    global server_names
    try:
        with open("serverNames.json", "r") as json_load:
            server_names = json.load(json_load)
    except:
        print("File not found/File doesn't exists.")

#Makes json file (serverNames.json) and puts server_names list in it
def makeJson():
    with open("serverNames.json", "w") as json_dump:
        json.dump(server_names, json_dump)

#Deletes one server specified in the parameter
def deleteServ(serv_to_delete):
    if serv_to_delete in server_names:
        server_names.remove(serv_to_delete)
    else:
        print("No such server")