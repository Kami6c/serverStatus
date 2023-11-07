import sys
from ping import myping
from servers import appendToList, makeJson, getJson, printServer, deleteServ
from serverInfo import addServerInfo, makeJsonServInfo, getJsonServInfo
from pingAll import pingAllServs



#CLI params
def shellMode():
    match sys.argv[1]:
        case "-m":
            print("Management mode adding server")
            getJson()
            appendToList(str(sys.argv[2]))
            makeJson()
            printServer()
        case "-c":
            print("Check server status mode")
            if len(sys.argv) > 3:
                check = myping(str(sys.argv[2]), int(sys.argv[3]))
            else:
                check = myping(str(sys.argv[2]))
                getJsonServInfo()
                addServerInfo(str(sys.argv[2]), check) 
                makeJsonServInfo()
        case "-d":
            getJson()
            deleteServ(str(sys.argv[2]))
            makeJson()
        case "-l":
            getJson()
            printServer()
        case "-a":
            print("test all")
            pingAllServs()
        case _:
            print("wrong letter")

#interactive
def interactiveMode():
    while True:   
        print("1 Add new server. 2 Delete a server. 3 Show servers. 4. Ping all servers. q. Quit")
        option = input("Option: ")
        match option:
            case "1":
                print("Adding server")
                getJson()
                serverName = input("Server name: ")
                appendToList(serverName)
                makeJson()
            case "2":
                print("Deleting server")
                getJson()
                servName = input("Server name: ")
                deleteServ(servName)
                makeJson()
            case "3": 
                getJson()
                printServer()
            case "4":
                pingAllServs()
            case "q":
                print("Exiting")
                break
            case _:
                print("Wrong option")
        
