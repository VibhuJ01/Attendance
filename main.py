from mark import mark,margin,display

import mysql.connector as ms
mycon = ms.connect(host="localhost",user="root",db="attendance",passwd="vibhu")
cur1 = mycon.cursor()

def main():
    
    print("1. Add a New Subject")
    print('2. Add a Old Subject')
    print("3. Mark Attendance")
    print('4. Add OD/ML')
    print("5. Remove Subject")
    print("6. Show Attendance")
    print("7. Exit")
    ch = input("What do you want to do? ")
    print("\n--------------------------------------------\n")

    
    if(ch == '1'):
        r,s = length()
        add(s)
        
    elif(ch == '2'):
        r,s = length()
        addE(s)

    elif(ch == '3'):
        do = input("Enter Day Order : ")
        print("\n--------------------------------------------\n")
        if(do >= '1' and do <= '5'): 
            mark(int(do))

        else:
            print('Wrong Input')
            print("\n--------------------------------------------\n")

    elif(ch == '4'):
        pass
    
    elif(ch == '5'):
        remove()
    
    elif(ch == '6'):
        display()
       
    elif(ch == '7'):
        print("Have a Nice Day")
        print("\n--------------------------------------------\n")
        return

    else:
        print("Wrong Input")
        print("\n--------------------------------------------\n")
    
    main()
    

            
def add(s):
    name = input('Name of your subject: ')
    sql = 'insert into att values(%s,%s,%s,%s,%s,%s,%s)'
    data = (s,name,0,0,0,0,0)
    cur1.execute(sql,data)
    mycon.commit()
    
    sql = 'insert into od values(%s,%s,%s,%s)'
    data = (s,0,0,0)
    cur1.execute(sql,data)
    mycon.commit()
    
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
        sql = 'insert into att values(%s,%s,%s,%s,%s,%s,%s)'
        data = [s,name,pre,ab,tot,perc,req]
        cur1.execute(sql,data)
        mycon.commit()


        perc,ab,req = margin(tot,pre+od+ml)
        sql = 'insert into od values(%s,%s,%s,%s)'
        data = [s,od,ml,perc]
        cur1.execute(sql,data)
        mycon.commit()
        
        print("Subject Added Succesfully")
        print("\n--------------------------------------------\n")
        
def remove():
    result,s = length()
    display()
    
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
        print('Subject Successfully Removed')
        print("\n--------------------------------------------\n")


        
def length():
    sql = 'select * from att'
    cur1.execute(sql)
    result = cur1.fetchall()
    return result,len(result)


if(__name__ == '__main__'):
    print("\n--------------------------------------------\n")
    main()

mycon.close()
