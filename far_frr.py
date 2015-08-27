import sys
from sys import getsizeof
x=1000000
original=[0]*x
imposter=[0]*x

impostercunt = 0 
originalcunt = 0 
filename="../L4.txt"

crr_out = open("../files/CRR.txt",'w')
flag  = 1
curs1 = 1 
curid = 1
mxs  =1
mxid =1
mxgi = 1
mxd = 1
mns = 1
mnid = 1
mnd = 1 

with open(filename,'r') as stream:
    
    for row in stream:
	data = row.split('\t')
	if len(data) != 6:
			break
	if flag == 1 : 
			curs = int(data[0])
			curid = int(data[1])
			mxs = int(data[2])
			mxid = int(data[3])
			mxgi = int(data[4])
			mns = mxs
			mxd = float(data[5].split("\n")[0])
			mnd = float(data[5].split("\n")[0])
			mnid =mxid
			flag = 0
	else :
			if curs != int(data[0]) or curid != int(data[1]):
                	        
				out='%d\t%d\t[(%d,%d)%.6f]\t[(%d,%d)%.6f]\t%.6f\t%d\n'%(curs,curid,mxs,mxid,mxd,mns,mnid,mnd,mxd/mnd,mxgi)	
				crr_out.write(out)				
				curs = int(data[0])
				curid = int(data[1])
				mxs = int(data[2])
				mxid = int(data[3])
				mns = mxs 
				mnid= mxid
				mxgi = int(data[4])	
				mxd = float(data[5].split("\n")[0])
				mnd = mxd
			else :
				score = float(data[5].split("\n")[0])
				if score < mxd:
					mxd = score 
					mxs =  int(data[2])
					mxid=  int(data[3])
					mxgi = int(data[4])
				if score > mnd:
					mnd = score 
					mns =  int(data[2])
					mnid=  int(data[3])
        score = 0 
	if len(data) == 6 :
       	 	score = float(data[5].split("\n")[0])*x
	else :
		break  
        intscore=int(score)  
	# Imposter  i index corresponds to  all values in between [ y*(i-1) , y*(i) ) 
	# Genuine i index corresponds to all values in between ( y*(i-1) , y*(i) ] 
	# y ==> pow( 10 , -6 )    
        if int(data[4])==1 :
            originalcunt+=1
            if score==intscore:
                if score!= 0:
                    original[intscore-1]+=1
                else:
                    original[intscore]+=1
            else:
                original[intscore]+=1
                 
        else:
	    impostercunt+=1
            if intscore==x:
                imposter[intscore-1]+=1
            else :
                imposter[intscore]+=1

	# Updated 
        # Imposter  i index corresponds to  all values in between [ 0, y*(i) ) 
	# Genuine i index corresponds to all values in between ( y*(i-1) , 1 ] 
	# y ==> pow( 10 , -6 )           
out='%d\t%d\t[(%d,%d)%.6f]\t[(%d,%d)%.6f]\t%.6f\t%d\n'%(curs,curid,mxs,mxid,mxd,mns,mnid,mnd,mxd/mnd,mxgi)

crr_out.write(out)
crr_out.close()

HG = open("../files/hist_G.txt",'w') 
HI = open("../files/hist_I.txt",'w')
for i in range(1,x):
	HI.write('%d' % i)
	HI.write(' ')
	HI.write('%f' % float(float(imposter[i])/float(impostercunt)))
	HI.write('\n')
	HG.write('%d' % i)
	HG.write(' ')
	HG.write('%f' % float(float(original[i])/float(originalcunt)))
	HG.write('\n')
HG.close()
HI.close()  
for i in range(1,x):
    imposter[i]=imposter[i-1]+imposter[i]
    

    
for i in range(x-2,-1,-1):
    original[i]=original[i+1]+original[i]

minvalue  = 1000000000000
threshold = 0 
for i in range(0,x):
	if imposter[i] != 0 and original[i] != 0 : 	
		if abs(float(imposter[i])/imposter[x-1] - float(original[i])/original[0] ) < minvalue : 
				minvalue = abs(float(imposter[i])/imposter[x-1] - float(original[i])/original[0]) 
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

frr = open("../files/FRR.txt",'w')  
far = open("../files/FAR.txt",'w') 
with open(filename,'r') as stream :
		for row1 in stream : 
			data1 = row1.split("\t") 
			if len(data1) != 6 :
				break 
			score = float(data1[5].split("\n")[0])
			if int(data1[4]) == 1:
					if score > threshold :
						far.write(row1)
						
			else :
					if score <= threshold :
						frr.write(row1)	
frr.close() 
far.close()
	


print threshold
imp = float(imposter[index])/imposter[x-1] 
orig= float(original[index])/imposter[x-1]
print imp
print orig
print abs(imp-orig) 


fout = open('../files/far_vs_frr.txt','w')

  
for i in range(0,x):
	fout.write(str(float(imposter[i])/imposter[x-1])+" "+str(float(original[i])/original[0])+'\n')


sts_file = """
**************************************************************************************************************************************
Genuine
===========================
177 data points
672.367 average
183.165 standard deviation
13.7675 standard error
**************************************************************************************************************************************
Imposter
===========================
165 data points
915.139 average
49.3979 standard deviation
3.84563 standard error
**************************************************************************************************************************************
Performance Parameters
===========================
Decidability Index        (DI) = 	~-1.80977784183226687455
Correct Recognition Rate (CRR) =   	100
Equal Error Rate         (EER) = 	 (2.695286)  0.890800 with Difference = 0.057239
**************************************************************************************************************************************
Failed Subject in Identification (CRR Failure)
===========================
+++++++++++++++++++++++++++++++++++++++++++++++++++++
Total Failed Subject =   0 (out of 100)
+++++++++++++++++++++++++++++++++++++++++++++++++++++
**************************************************************************************************************************************
+++++++++++++++++++++++++++++++++++++++++++++++++++++
Total No. of Falsely Reject Matching =   9 out of total 300 genuine matching
+++++++++++++++++++++++++++++++++++++++++++++++++++++
**************************************************************************************************************************************
+++++++++++++++++++++++++++++++++++++++++++++++++++++
Total No. of Falsely Accept Matching =   808 out of total 29700 imposter matching
+++++++++++++++++++++++++++++++++++++++++++++++++++++
**************************************************************************************************************************************
Actual Performance Parameters
===========================
False Acceptance Rate        (FAR) = 		~2.72053872053872053872
False Rejection  Rate        (FAR) = 		3
**************************************************************************************************************************************
"""
