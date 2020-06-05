import time

def startStoppeklokke():
    global ms
    ms=round(time.time()*1000.0)

def stopStoppeklokke():
    global ms
    return round(time.time()*1000.0)-ms #skal få antall ms siden vi startet klokken

def sovms(millisekunder):
    time.sleep(millisekunder/1000)

def getUkedag():
    """Leser/får tak i ukedagen til intern klokke på norsk"""
    day=time.strftime("%a")
    if day== "Mon":return "mandag"
    elif day=="Tue":return "tirsdag"
    elif day=="Wed":return "onsdag"
    elif day=="Thu":return "torsdag"
    elif day=="Fri":return "fredag"
    elif day=="Sat":return "lørdag"
    elif day=="Sun":return "søndag"
#end getUkedag

def getTimeStr():
    timen=str((time.strftime('%H')))
    return (timen)

def getTimeNum():
    timen=int(time.strftime('%H'))
    return(timen)

def getMinStr():
    minuttet=str(time.strftime("%M"))
    return minuttet
#end getMinStr

def getMinNum():
    minuttet=int(time.strftime("%M"))
    return minuttet
#end getMinNum
    
def getSekStr():
    sek=str(time.strftime('%S'))
    return(sek)

def getSekNum():
    sek=int(time.strftime('%S'))
    return(sek)

def getDatoStr():
    datoen=str(time.strftime("%m"))
    return datoen
#end getDatoStr

def getDatoNum():
    datoen=int(time.strftime("%m"))
    return datoen
#end getDatoNum

def getÅrStr():
    år=str(time.strftime('%Y'))
    return(år)

def getÅrStr():
    år=int(time.strftime('%Y'))
    return(år)










    


