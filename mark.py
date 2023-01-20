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

    try:

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
                
                    
        if(ch == 1):
            pass
        
        elif(ch == 2):
            pass
        
        elif(ch == 3):
            for i in dict.keys():
                print(i, end = ' ')
            
            sub = input("Choose subject from the given list ")
            hrs = dict[sub]
   
        else:
            print("wrong Input")
            print("\n--------------------------------------------\n") 
                
    except:
        print("\n--------------------------------------------\n")
        print("Wrong Input")
        print("\n--------------------------------------------\n")
        
