from tabulate import tabulate

import mysql.connector as ms
mycon = ms.connect(host="localhost",user="root",db="attendance",passwd="vibhu")
cur1 = mycon.cursor()


def mark(do):
    l=[
        ['RL_Lab','RL_Lab','RL','ISPA','Eco_Impact','Eco_Impact','Design_of_AI'],
        ['Cognitive_Science','Cognitive_Science','Design_of_AI','Design_of_AI','ISPA'],
        ['Design_of_AI_lab','Design_of_AI_lab','Text_Analysis ','RL','Maths'],
        ['Maths','Maths','Cognitive_Science','Text_Analysis '],
        ['ESP','ESP','Text_Analysis ','Eco_Impact','Maths']
      ]

##    try:
    print("1. Present All Day")
    print("2. Absent All Day")
    print("3. Custom Marking")
    print('4. Back')
    ch = int(input("Enter your choice : "))
    print("\n--------------------------------------------\n")

    if(ch == 4):
        return
    
    dict = {}
    for i in range(len(l[do-1])):
        if l[do-1][i] in dict:
            dict[l[do-1][i]]+=1
            
        else:
            dict[l[do-1][i]]=1
       
    sql = 'select * from att'
    cur1.execute(sql)
    result = cur1.fetchall()
    l = len(result)
    
    hours =  list(dict.values())
    name = list(dict.keys())  
    if(ch == 1):
        present(hours,name,result,l)
        print('Present Successfully Marked')
        print("\n--------------------------------------------\n")
        display()
                    
    elif(ch == 2):
        absent(hours,name,result,l)
        print('Absent Successfully Marked')
        print("\n--------------------------------------------\n")
        display()
    
    elif(ch == 3):
        for i in dict.keys():
            print(i, end = ' ')
        
        sub = input("Choose subject from the given list ")
        hrs = dict[sub]

    else:
        print("wrong Input")
        print("\n--------------------------------------------\n")
                
##    except:
##        print("\n--------------------------------------------\n")
##        print("Wrong Input")
##        print("\n--------------------------------------------\n")


def present(hours,name,result,l):
    for i in range(l):
        for j in range(len(name)):
            if(result[i][1] == name[j]):
                tot = hours[j] + result[i][4]
                pre = hours[j] + result[i][2]
                perc,ab,req = margin(tot,pre)

                sql = '''update att
                         set present = %s,
                         total = %s,
                         percentage = %s,
                         req_margin = %s
                         where sub_name = %s
                      '''
                data = [pre,tot,perc,req,name[j]]
                cur1.execute(sql,data)
                mycon.commit()
                update_od(result[i][0],pre,tot)

def absent(hours,name,result,l):
    for i in range(l):
        for j in range(len(name)):
            if(result[i][1] == name[j]):
                tot = hours[j] + result[i][4]
                pre = result[i][2]
                perc,ab,req = margin(tot,pre)

                sql = '''update att
                         set absent = %s,
                         total = %s,
                         percentage = %s,
                         req_margin = %s
                         where sub_name = %s
                      '''
                data = [ab,tot,perc,req,name[j]]
                cur1.execute(sql,data)
                mycon.commit()
                update_od(result[i][0],pre,tot)
                
def update_od(s,pre,tot):
    sql = 'select * from od'
    cur1.execute(sql)
    result = cur1.fetchall()

    for i in result:
        if(i[0] == s):
            perc,ab,req = margin(tot,pre+i[1]+i[2])
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
