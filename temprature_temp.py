import os
import time
import glob
import MySQLdb
def log_temperature(temp):
 db = MySQLdb.connect('localhost','tempuser','temp',db='temp');
 cursor = db.cursor();
 date=time.strftime("%Y-%m-%d")
 t=time.strftime("%H:%M:%S")
 print(date+""+t)
 try:
   cursor.execute("INSERT INTO logger VALUES(%s,%s,%s)",(date,t,temp))
   db.commit()
 except:
   print("ERROR")
   db.rollback()
   db.close()
 return None

def get_temp(devicefile):
    try:
        fileobj = open(devicefile,'r')
        lines = fileobj.readlines()
        fileobj.close()
    except:
        return None
    status = lines[0][-4:-1]

    if status=="YES":
        tempstr= lines[1][-6:-1]
        tempvalue=float(tempstr)/1000
        return tempvalue
    else:
        print "There was an error."
        return None
while 1:
    os.system('sudo modprobe w1-gpio')
    os.system('sudo modprobe w1-therm')
    devicelist = glob.glob('/sys/bus/w1/devices/28*')
if devicelist!='':
        w1device = devicelist[0] + '/w1_slave'
    temp = get_temp(w1device)

    temperature = get_temp(w1device)
    print "temperature="+str(temp)
    log_temperature(temp)

