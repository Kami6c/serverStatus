from ping3 import ping, verbose_ping

def myping(host, pingCount=4):
    verbose_ping(host, count=pingCount)
    resp = ping(host)
    if resp == False or resp == None:
        return False
    else:
        return True
