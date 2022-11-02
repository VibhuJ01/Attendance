from tabulate import tabulate
import mysql.connector as ms
mycon = ms.connect(host="localhost",user="root",db="attendance",passwd="vibhu")
cur1 = mycon.cursor()

def main():
    
    print("1. Add a new subject")
    print('2. Add Already Existed Subject')
    print("3. Mark Attendance")
    print("4. Remove Subject")
    print("5. Show Attendance")
    print("6. Exit")
    ch = input("What do you want to do? ")
    print("\n--------------------------------------------\n")
    
    
    if(ch == '1'):
        s = length(ch)
        add(s)
        
    elif(ch == '2'):
        s = length('1')
        addE(s)

    elif(ch == '3'):
        pass
    
    elif(ch == '4'):
        remove()
    
    elif(ch == '5'):
        length(ch)
       
    elif(ch == '6'):
        print("Have a Nice Day")
        print("\n--------------------------------------------\n")
        return

    else:
        print("Wrong Input")
        print("\n--------------------------------------------\n")
    
    main()
    
def length(ch):
    sql = 'select * from att'
    cur1.execute(sql)
    result = cur1.fetchall()

    if(ch == '1'):
        return len(result)

    elif(ch == '5'):
        if(len(result) == 0):
            print("No Subject is Added")
            print("\n--------------------------------------------\n")

        else:
            keys = ['Serial_NO','Name','Present','Absent','Total','Percentage','Required/Margin']
            print(tabulate(result, headers = keys, tablefmt = 'pretty',showindex = False))
            print("\n--------------------------------------------\n")
            return result
            
def add(s):
    name = input('Name of your subject: ')
    sql = 'insert into att values(%s,%s,%s,%s,%s,%s,%s)'
    data = (s,name,0,0,0,0,0)
    cur1.execute(sql,data)
    mycon.commit()
    print("\n--------------------------------------------\n")
    print("Subject Added Succesfully")
    print("\n--------------------------------------------\n")

def remove():
    result = length('5')

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
        sql = 'delete from att where serial =' + str(ch)
        cur1.execute(sql)
        mycon.commit()
        print('Subject Successfully Removed')
        print("\n--------------------------------------------\n")

def addE(s):
    name = input('Name of your subject: ')
    print("\n--------------------------------------------\n")
    try:
        tot = int(input('Total: '))
        print("\n--------------------------------------------\n")
        pre = int(input('Present: '))
        print("\n--------------------------------------------\n")
        perc = (pre/tot)*100
        perc = round(perc,2)
        ab = tot-pre
        req = (ab*4) - tot

    except:
        print("\n--------------------------------------------\n")
        print("Wrong Input")
        print("\n--------------------------------------------\n")
        
    else:
        if(req < 0):
            i = 0
            while((ab+i)*4 < tot+i):
                i+=1
                
            req = i
                
        sql = 'insert into att values(%s,%s,%s,%s,%s,%s,%s)'
        data = (s,name,pre,ab,tot,perc,req)
        cur1.execute(sql,data)
        mycon.commit()
        print("Subject Added Succesfully")
        print("\n--------------------------------------------\n")

    
if(__name__ == '__main__'):
    print("\n--------------------------------------------\n")
    main()

mycon.close()
