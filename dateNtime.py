import datetime

def getTime():
    time = datetime.datetime.now()
    return time.strftime("%H:%M:%S")

def getDate():
    date = datetime.datetime.now()
    return date.strftime("%d/%m/%Y")