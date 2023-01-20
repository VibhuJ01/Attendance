l=[
    ['rl_lab','rl_lab','A1','A2','F','F','G2'],
    ['B','B','G1','Gl','A1'],
    ['AI_lab','AI_lab','C','C','A2','D','B'],
    ['D','D','B','E2','C','MOOC','MOOC'],
    ['E1','E1','C','F','D']
  ]

try:
    do = int(input("Enter Day Order : "))
    if do>=1 and do<=5: 
        print("1. Present All Day")
        print("2. Absent All Day")
        print("3. Custom Marking")

        c = int(input("Enter your choice : "))
        
        d={}
        for i in range(len(l[do-1])):
            if l[do-1][i] in d:
                d[l[do-1][i]]+=1
            else:
                d[l[do-1][i]]=1

        if c==1:
            
        elif c==2:

        elif c==3:
            print(d.keys(),end='\n')
            sub = input("Choose subject from the given list ")
            hrs = d[sub]
        else:
            print("wrong choice")
except:
    print("Wrong Choice")
