import datetime
#Getting Time in 24:59:59 format
def getTime():
    time = datetime.datetime.now()
    return time.strftime("%H:%M:%S")

#Getting Date in Day/Month/Year format
def getDate():
    date = datetime.datetime.now()
    return date.strftime("%d/%m/%Y")