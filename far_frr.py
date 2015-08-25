x=1000000
original=[0]*x
imposter=[0]*x

with open("L4_1000.txt",'r') as stream:
    
    for row in stream:
        data=row.split("\t")
        score = float(data[5].split("\n")[0])*1000000
        intscore=int(score)  
	# Imposter  i index corresponds to  all values in between [ y*(i-1) , y*(i) ) 
	# Genuine i index corresponds to all values in between ( y*(i-1) , y*(i) ] 
	# y ==> pow( 10 , -6 )    
        if int(data[4])==1 :
            if score==intscore:
                if score!= 0:
                    original[intscore-1]+=1
                else:
                    original[intscore]+=1
            else:
                original[intscore]+=1
                 
        else:
		
            if intscore==x:
                imposter[intscore-1]+=1
            else :
                imposter[intscore]+=1

	# Updated 
        # Imposter  i index corresponds to  all values in between [ 0, y*(i) ) 
	# Genuine i index corresponds to all values in between ( y*(i-1) , 1 ] 
	# y ==> pow( 10 , -6 )           
  
for i in range(1,x):
    imposter[i]=imposter[i-1]+imposter[i]
    

    
for i in range(x-2,-1,-1):
    original[i]=original[i+1]+original[i]



print imposter

