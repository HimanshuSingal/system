original=[0]*1000001
imposter=[0]*1000001

with open("L4_1000.txt",'r') as stream:
    chk=1
    for row in stream:
        data=row.split("\t")
        score = float(data[5].split("\n")[0])*1000000
        
        intscore=int(score)
          
        if int(data[4])==1 :
            if score==intscore:
                if score!= 0:
                    original[intscore-1]+=1
                else:
                    original[intscore]+=1
            else:
                original[intscore]+=1
        else:
            imposter[intscore]+=1
        if(chk==10):
            break
        chk=chk+1   
for i in range(1,1000001):
    imposter[i]=imposter[i-1]+imposter[i]
    

    
for i in range(1000001-2,-1,-1):
    original[i]=original[i+1]+original[i]

print imposter

