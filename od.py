from mark import update_od

import mysql.connector as ms
mycon = ms.connect(host="localhost",user="root",db="attendance",passwd="vibhu")
cur1 = mycon.cursor()

def od_ml():
    print('1. OD')
    print('2. ML')
    print('3. Back')
    ch = input("What do you want to do? ")
    print("\n--------------------------------------------\n")
     
    if(ch == '3'):
        return

    elif(ch == '1'):
        od = 'OD'

    elif(ch == '2'):
        od = 'ML'

    else:
        print("Wrong Input")
        print("\n--------------------------------------------\n")

    return od

def marking(od,l):

    try:
        s = int(input('Enter Serial Number: '))
        if(s<0 or s>l):
            print("\n--------------------------------------------\n")
            print("Wrong Input")
            print("\n--------------------------------------------\n")
            return
            
        h = int(input('Enter Number of Hours: '))
        
        print("\n--------------------------------------------\n")
        ans = input('Are you sure?(y/n) ')
        print("\n--------------------------------------------\n")
        
        if(ans.lower() != 'y'):
            print("Wrong Input")
            print("\n--------------------------------------------\n")
        
    except:
        print("\n--------------------------------------------\n")
        print("Wrong Input")
        print("\n--------------------------------------------\n")

    else:

        if(od == 'OD'):
            sql = '''update od
                     set od_hours = od_hours + %s
                     where serial_no = %s
                     '''
        else:
            sql = '''update od
                     set ml_hours = ml_hours + %s
                     where serial_no = %s
                     '''
        
        data = [h,s]
        cur1.execute(sql,data)
        mycon.commit()

        sql = 'select * from att'
        cur1.execute(sql)
        result = cur1.fetchall()

        update_od(s,result[s][2],result[s][4])

        print("OD/ML marked Successfully")
    
            
