import sys
from modes import shellMode, interactiveMode
import argparse

def options():
    parser = argparse.ArgumentParser(description="Simple Ping Program")
    parser.add_argument("-m", action="help", help="Adds a server. (Usage: -m server_name)")
    parser.add_argument("-c", action="help", help="Checks and adds server to the server list. (Usage: -c server_name)")
    parser.add_argument("-d", action="help", help="Deletes specified server. (Usage: -d server_name)")
    parser.add_argument("-a", action="help", help="Pings and adds all the servers to the server list file. (Usage: -a)")
    parser.add_argument("-l", action="help", help="Lists all the servers in a server list file. (Usage: -l)")
    args = parser.parse_args()

    return args



if len(sys.argv) > 1:
    if(sys.argv[1] == "--help"):
        options()
    else:
        shellMode()
else:
    interactiveMode()


    
    
