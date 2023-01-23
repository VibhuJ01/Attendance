from tabulate import tabulate

import mysql.connector as ms
mycon = ms.connect(host="localhost",user="root",db="attendance",passwd="vibhu")
cur1 = mycon.cursor()


def mark():
    timetable=[
        ['RL_Lab','RL_Lab','RL','ISPA','Eco_Impact','Eco_Impact','Design_of_AI'],
        ['Cognitive_Science','Cognitive_Science','Design_of_AI','Design_of_AI','ISPA'],
        ['Design_of_AI_lab','Design_of_AI_lab','Text_Analysis','Text_Analysis','RL','Maths'],
        ['Maths','Maths','Cognitive_Science','Text_Analysis'],
        ['ESP','ESP','Eco_Impact','Maths']
      ]

    try:
        print("1. Present All Day")
        print("2. Absent All Day")
        print("3. Custom Marking")
        print('4. Back')
        ch = int(input("Enter your choice : "))
        print("\n--------------------------------------------\n")

        if(ch == 4):
            return

    #--------------------------------------------
        
        sql = 'select * from att'
        cur1.execute(sql)
        result = cur1.fetchall()
        l = len(result)
        
    #--------------------------------------------
        
        if(ch == 3):
            ans = 'y'
            while(ans.lower() == 'y'):
                display()
                s = int(input('Enter Serial Number: '))
                print("\n--------------------------------------------\n")
                print('Enter Number of Hours in -ve for absent')
                print("\n--------------------------------------------\n")
                h = int(input('Enter Number of Hours: '))

                if(h>=0):
                    present(result[s][2]+h,result[s][4]+h,result[s][1],result[s][0])

                else:
                    h = -1*h
                    absent(result[s][2],result[s][4]+h,result[s][1],result[s][0])
                print("\n--------------------------------------------\n")
                print("Attendance Update Successfully")
                print("\n--------------------------------------------\n")
                display()
                ans = input('Do you want to Continue(y/n): ')
                print("\n--------------------------------------------\n")
                
            return
        
    #--------------------------------------------
        
        do = input("Enter Day Order : ")
        do = int(do)
        print("\n--------------------------------------------\n")
        if(do >= 1 and do <= 5):
            dict = {}
            for i in range(len(timetable[do-1])):
                if timetable[do-1][i] in dict:
                    dict[timetable[do-1][i]]+=1
                    
                else:
                    dict[timetable[do-1][i]]=1

            hours =  list(dict.values())
            name = list(dict.keys())
            
        else:
            print("Wrong Input")
            print("\n--------------------------------------------\n")
            return
        
    #--------------------------------------------
         
        if(ch == 1):
            
            marking(hours,name,result,l,0)
            print('Present Successfully Marked')
            print("\n--------------------------------------------\n")
            display()
                        
        elif(ch == 2):
            marking(hours,name,result,l,1)
            print('Absent Successfully Marked')
            print("\n--------------------------------------------\n")
            display()
        
        

        else:
            print("Wrong Input")
            print("\n--------------------------------------------\n")
                
    except:
        print("\n--------------------------------------------\n")
        print("Wrong Input")
        print("\n--------------------------------------------\n")


def marking(hours,name,result,l,n):
    for i in range(l):
        for j in range(len(name)):
            if(result[i][1] == name[j]):
                tot = hours[j] + result[i][4]
                
                if(n == 0):
                    pre = result[i][2] + hours[j]
                    present(pre,tot,name[j],result[i][0])

                else:
                    pre = result[i][2]
                    absent(pre,tot,name[j],result[i][0])
                
                
def present(pre,tot,sub,n):
    perc,ab,req = margin(tot,pre)
    sql = '''update att
             set present = %s,
             total = %s,
             percentage = %s,
             req_margin = %s
             where sub_name = %s
          '''
    data = [pre,tot,perc,req,sub]
    cur1.execute(sql,data)
    mycon.commit()
    update_od(n,pre,tot)

def absent(pre,tot,sub,n):
    perc,ab,req = margin(tot,pre)
    sql = '''update att
             set absent = %s,
             total = %s,
             percentage = %s,
             req_margin = %s
             where sub_name = %s
          '''
    data = [ab,tot,perc,req,sub]
    cur1.execute(sql,data)
    mycon.commit()
    update_od(n,pre,tot)
                
def update_od(s,pre,tot):
    sql = 'select * from od'
    cur1.execute(sql)
    result = cur1.fetchall()

    for i in result:
        if(i[0] == s):
            
            perc,ab,req = margin(tot,pre+int(i[2])+int(i[3]))
            sql = '''update od
                     set n_p = %s
                     where serial_no = %s
                  '''
            data = [perc,s]
            cur1.execute(sql,data)
            mycon.commit()
                
def display():
    sql = '''select a.*,o.od_hours,o.ml_hours,o.n_p from att a join od o
            on a.Serial_no = o.Serial_no'''
    
    cur1.execute(sql)
    result = cur1.fetchall()
    
    if(len(result) == 0):
        print("No Subject is Added")
        print("\n--------------------------------------------\n")

    else:
        keys = ['Serial_NO','Name','Present','Absent','Total','Percentage','Required/Margin','OD','ML','Percentage_OD']
        print(tabulate(result, headers = keys, tablefmt = 'pretty',showindex = False))
        print("\n--------------------------------------------\n")
        

def margin(tot,pre):
    perc = (pre/tot)*100
    perc = round(perc,2)
    ab = tot-pre

    if(perc == 100):
        req = 0

    else:
        req = (ab*4) - tot

    if(req < 0):
        i = 0
        while((ab+i)*4 < tot+i):
            i+=1  
        req = i
        
    else:
        req = -1*req

    return perc,ab,req

def length():
    sql = 'select * from att'
    cur1.execute(sql)
    result = cur1.fetchall()
    return result,len(result)

            
def add(s):
#--------------------------------------------
    name = input('Name of your subject: ')
    sql = 'insert into att values(%s,%s,%s,%s,%s,%s,%s)'
    data = (s,name,0,0,0,0,0)
    cur1.execute(sql,data)
    mycon.commit()
#--------------------------------------------    
    sql = 'insert into od values(%s,%s,%s,%s,%s)'
    data = (s,name,0,0,0)
    cur1.execute(sql,data)
    mycon.commit()
#--------------------------------------------    
    print("\n--------------------------------------------\n")
    print("Subject Added Succesfully")
    print("\n--------------------------------------------\n")

def addE(s):
    name = input('Name of your subject: ')
    print("\n--------------------------------------------\n")
    try:
        tot = int(input('Total: '))
        pre = int(input('Present: '))
        print("\n--------------------------------------------\n")
        perc,ab,req = margin(tot,pre)

        od = int(input('Od Hours: '))
        ml = int(input('ML Hours: '))
        print("\n--------------------------------------------\n")
        
    except:
        print("\n--------------------------------------------\n")
        print("Wrong Input")
        print("\n--------------------------------------------\n")
        
    else:
#--------------------------------------------
        sql = 'insert into att values(%s,%s,%s,%s,%s,%s,%s)'
        data = [s,name,pre,ab,tot,perc,req]
        cur1.execute(sql,data)
        mycon.commit()
#--------------------------------------------
        perc,ab,req = margin(tot,pre+od+ml)
        sql = 'insert into od values(%s,%s,%s,%s,%s)'
        data = [s,name,od,ml,perc]
        cur1.execute(sql,data)
        mycon.commit()
#--------------------------------------------        
        print("Subject Added Succesfully")
        print("\n--------------------------------------------\n")
        
def remove():
    result,s = length()
    display()

    if(s == 0):
        return
    
    try:
        ch = int(input("Serial Number of Subject you want to Remove: "))
        print("\n--------------------------------------------\n")
        for i in result:
            if(i[0] == ch):
                break
        else:
            print('Serial Number is not Present')
            print("\n--------------------------------------------\n")
            return

    except:
        print("\n--------------------------------------------\n")
        print("Wrong Input")
        print("\n--------------------------------------------\n")

    else:
        sql = 'delete from att where Serial_no =' + str(ch)
        cur1.execute(sql)
        mycon.commit()

        sql = 'delete from od where Serial_no =' + str(ch)
        cur1.execute(sql)
        mycon.commit()
        print('Subject Successfully Removed')
        print("\n--------------------------------------------\n")


