import sqlite3
def india():
    print "Enter the mobile number"
    n = raw_input()
    l = []
    l = n
    le = len(l)
    num = l[0:4]
    con = sqlite3.connect('data.db')
    cursor = con.cursor()
    nam1 = ("SELECT * FROM mobileNumberfinder where mobilenumber = ?")
    cursor.execute(nam1, [(num)])
    result = cursor.fetchall()
    if result:
        for i in result:
            print "SERVICE PROVIDER IS :",i[1]
            print "LOCATION IS         :",i[2]
            print "LATITUDE :",i[4],"LONGITUDE :",i[5]
def other():
    print "Enter the mobile number"
    n = raw_input()
    l = []
    l = n
    le = len(l)
    num = l[0:3]
    con = sqlite3.connect('data.db')
    cursor = con.cursor()
    nam1 = ("SELECT * FROM mobileNumberfinder where mobilenumber = ?")
    cursor.execute(nam1, [(num)])
    result = cursor.fetchall()
    if result:
        for i in result:
            print "SERVICE PROVIDER IS :", i[1]
            print "LOCATION IS         :", i[2]
            print "LATITUDE :", i[4], "LONGITUDE :", i[5]

def isd():
    print "ENTER THE ISD CODE"
    n = raw_input()
    l = []
    l = n
    le = len(l)
    num = l[0:4]
    con = sqlite3.connect('data.db')
    cursor = con.cursor()
    nam1 = ("SELECT * FROM isdcodes where isdcode = ?")
    cursor.execute(nam1, [(num)])
    result = cursor.fetchall()
    print "LOCATIONS :"
    if result:
        for i in result:
            print i[0]

def std():
    print "ENTER THE STD CODE"
    n = raw_input()
    l = []
    l = n
    le = len(l)
    num = l[0:4]
    con = sqlite3.connect('data.db')
    cursor = con.cursor()
    nam1 = ("SELECT * FROM stdcodes where stdcode = ?")
    cursor.execute(nam1, [(num)])
    result = cursor.fetchall()
    if result:
        for i in result:
            print "LOCATION IS:",i[0]

print "FIND LOCATION AND SERVICE PROVIDER OF MOBILE NUMBER AND FIND LOCATION VIA STD & ISD \n"
print "SELECT A POTION"
print "1=>FIND LOCATION AND SERVICE PROVIDER OF MOBILE NUMBER 2=>FIND LOCATION VIA STD & ISD"
a = input()
if a==1:
    print "SELECT YOUR COUNTRY"
    print "1=>INDIA 2=>US 3=>CANDA 4=>PAKISTAN"
    x =input()
    if x==1:
        india()
    elif 1<x<=4:
        other()
    else:
        print "INVALID INPUT"
elif a==2:
    print "SELECT STD OR ISD"
    print "1=>STD 2=>ISD"
    y= input()
    if y==1:
        std()
    elif y==2:
        isd()
    else:
        print "INVALID INPUT"
else:
    print "INVALID INPUT"
