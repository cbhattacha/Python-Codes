def QuestionsMarks(s):
    l = len(s)
    lsnum = []
    ind = []
    flag=0
    count=0
    for i in range(l):
        count=0
        if s[i].isdigit() == True:
            lsnum.append(s[i])
            ind.append(i)
            if len(lsnum)== 2:
                if (int(lsnum[0])+int(lsnum[1])) == 10:
                    flag=1
                    for item in range(ind[0]+1,ind[1]):
                        if s[item] == '?':
                            count+=1
                    if count == 3:
                        print("True")
                    else:  
                        print("False") 
                ind = []
                lsnum = []
    
    if flag == 0:   #There aren't nums that add to 10 or 
        print("False")          #There aren't 3 consequetive ?
                
s = input("Please input any string:\n")
print('Entered string: ',s)
QuestionsMarks(s)
