from mark import mark,display,length,add,addE,remove
from od import od_ml,marking


import mysql.connector as ms
mycon = ms.connect(host="localhost",user="root",db="attendance",passwd="vibhu")
cur1 = mycon.cursor()

def main():
    
    print("1. Mark Attendance")
    print('2. Add OD/ML')
    print("3. Show Attendance")
    print("4. Add a New Subject")
    print('5. Add a Old Subject')
    print("6. Remove Subject")
    print("7. Exit")
    ch = input("What do you want to do? ")
    print("\n--------------------------------------------\n")

    if(ch == '1'):
        mark()

    elif(ch == '2'):
        od = od_ml()
        display()
        res,l = length()
        marking(od,l)
        display()
    
    elif(ch == '3'):
        display()
        
    elif(ch == '4'):
        r,s = length()
        add(s)
        
    elif(ch == '5'):
        r,s = length()
        addE(s)

    elif(ch == '6'):
        remove()
     
    elif(ch == '7'):
        print("Have a Nice Day")
        print("\n--------------------------------------------\n")
        return

    else:
        print("Wrong Input")
        print("\n--------------------------------------------\n")
    
    main()
    

if(__name__ == '__main__'):
    print("\n--------------------------------------------\n")
    main()

mycon.close()
