import sys
from sys import getsizeof
x=1000000
original=[0]*x
imposter=[0]*x

with open("L4_1000.txt",'r') as stream:
    
    for row in stream:
        data=row.split("\t")
	score = 0 
	if len(data) == 6 :
       	 	score = float(data[5].split("\n")[0])*x
	else :
		continue 
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

minvalue  = 1000000000000
threshold = 0 
for i in range(0,x):
	if imposter[i] != 0 and original[i] != 0 : 	
		if abs(int(imposter[i]/imposter[x-1]) - int(original[i]/original[0]) ) < minvalue : 
				minvalue = abs(imposter[i]/imposter[x-1] - original[i]/original[0]) 
				threshold = i*(pow(10,-6)) 
				index = i 
mI = x 
mG = x
xI = -1
xG = -1

if threshold == 0 :
	for i in range(0,x):
		if imposter[i] != 0:
			mI = i 
			break
	for i in range(x-1,-1,-1):
		if imposter[i] != 0:
			xI = i 
			break
	for i in range(0,x):
		if original[i] != 0:
			mG = i 
			break
	for i in range(x-1,-1,-1):
		if original[i] != 0:
			xG = i 
			break
	if abs(xG - mI) < abs(xI - mG) :
			threshold = (abs(xG+mI)/2)*(pow(10,-6)) 
			index = (abs(xG+mI)/2)
	else:
			threshold = (abs(xI+mG)/2)*(pow(10,-6))
			index = (abs(xI+mG)/2)

print threshold
print imposter[index] 
print original[index]
print abs(imposter[index]-original[index]) 
