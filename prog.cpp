#include <bits/stdc++.h>
#include <fstream>
#include <iostream>
#include <stdio.h>
#include <math.h>
#include <string>
#define x 1000000
#include <algorithm>
using namespace std;
int main()
{
  //  ios::sync_with_stdio(false) ; 
  int original[x]={0};
  int imposter[x]={0};
  ifstream infile;
  ofstream outfile;
  int idp = 0 ;
  int impostercunt=0 ;
  int originalcunt=0 ;
  int gdp = 0 ;
  int frrcunt = 0;
  int farcunt = 0 ;
  int tot = 0 ;
  int crr = 0  ;
  int failsub = 0 ; 
  infile.open("../L4.txt");
  outfile.open("../files/CRR.dat");
  int curs;
  int flag  = 1;
  int curs1 = 1 ;

  int curid = 1;
  int mxs  =1;
  int mxid =1;
  int mxgi = 1;
  float mxd = 1;
  int mns = 1;
  int mnid = 1;
  float mnd = 1 ;
float data[6];
 
 char buffer[1000];
 float score;
 cout << "started\n" ;  
 while(!infile.eof())
    {
      
    
      infile>>data[0]>>data[1]>>data[2]>>data[3]>>data[4]>>data[5];
      if(flag==1)
	{
	  curs = int(data[0]);
	  curid = int(data[1]);
	  mxs = int(data[2]);
	  mxid = int(data[3]);
	  mxgi = int(data[4]);
	  mns = mxs;
	  mxd = data[5];
	  mnd = mxd;
	  mnid =mxid;
	  flag = 0;
	}
      else
	{
	  if( curs != int(data[0]) or curid != int(data[1]))
	    {
	      if(int(mxgi) == 1)crr++ ;
	      tot++;
	      sprintf(buffer,"%d\t%d\t[(%d,%d)%.6f]\t[(%d,%d)%.6f]\t%.6f\t%d\n",curs,curid,mxs,mxid,mxd,mns,mnid,mnd,mxd/mnd,mxgi);
	      outfile<<buffer;
	      curs = int(data[0]);
	      curid = int(data[1]);
	      mxs = int(data[2]);
	      mxid = int(data[3]);
	      mns = mxs ;
	      mnid= mxid;
	      mxgi = int(data[4]);
	      mxd = data[5];
	      mnd = mxd;
	    }
	  else
	    {
	      score = data[5];
	      if(score < mxd)
		{
		  mxd = score; 
		  mxs =  int(data[2]);
		  mxid=  int(data[3]);
		  mxgi = int(data[4]);
		}
	      if(score > mnd)
		{
		  mnd = score; 
		  mns =  int(data[2]);
		  mnid=  int(data[3]);
		}
	    }
	}
      
      score = data[5]*x;
      int intscore=int(score);  
	// Imposter  i index corresponds to  all values in between [ y*(i-1) , y*(i) ) 
	//	# Genuine i index corresponds to all values in between ( y*(i-1) , y*(i) ] 
	//	# y ==> pow( 10 , -6 )    
	if(int(data[4])==1)
	  {
	    originalcunt+=1;
		if(score!= 0)
		  original[intscore-1]+=1;
		else
		  original[intscore]+=1;
	  }
	else
	  {
	    impostercunt+=1;
	    if(intscore==x){
	      imposter[intscore-1]+=1;
	      // printf("%d\t%d\n",intscore-1,imposter[intscore-1]);
	    }
	    else {
	      imposter[intscore]+=1;
	      // printf("%d \t %d \n",intscore,imposter[intscore]);
	    }
	  }
	
      //	Updated 
      //         Imposter  i index corresponds to  all values in between [ 0, y*(i) ) 
      //	 Genuine i index corresponds to all values in between ( y*(i-1) , 1 ] 
      //	 y ==> pow( 10 , -6 )           
    }
  sprintf(buffer,"%d\t%d\t[(%d,%d)%.6f]\t[(%d,%d)%.6f]\t%.6f\t%d\n",curs,curid,mxs,mxid,mxd,mns,mnid,mnd,mxd/mnd,mxgi);
  outfile<<buffer;
  outfile.close();
  infile.close();
  cout << "crr done\n";
  ofstream hg ;
  hg.open("../files/hist_G.txt");
  ofstream hi;
  hi.open("../files/hist_I.txt");
  
  for(int i=0;i<x;i++)
    {
      if(imposter[i]!=0)idp++;
      if(original[i]!=0)gdp++;
      hi<<i<<" "<<(imposter[i]*1.0)/impostercunt<<"\n";
      hg<<i<<" "<<(original[i]*1.0)/originalcunt<<"\n";
         
    }
  cout << "hist done\n";
  hg.close();
  hi.close();
  for(int i=1;i<x;i++)
    imposter[i]=imposter[i-1]+imposter[i];
  for(int i=x-2;i>=0;i--)
    original[i]=original[i+1]+original[i];


  
  float  minvalue  = 1000000.00 ;
  float threshold = 0 ;
  int index ;
  for(int i=0;i<x;i++){
    if (imposter[i] != 0 && original[i] != 0 ){
      if (fabs( float( float(imposter[i]) / (float( imposter[x-1])) ) - float( float(original[i]) / (float( original[0])) ) ) < minvalue ){ 
	minvalue = fabs((imposter[i]*(1.000000))/(imposter[x-1]*1.000000) -   (1.000000*original[i])/(1.000000*original[0])); 
	threshold = float((float)i*(float(pow(10,-6))));
	  index = i ;
      }
    }
  }
  int mI = x; 
  int mG = x;
  int xI = -1;
  int xG = -1;

  if (threshold == 0 ){
    for (int i=0;i<x;i++){
      if (imposter[i] != 0){
       		mI = i ;
		break;
      }
      }
    for (int i=x-1;i>=0;i--){
      if (imposter[i] != 0){
	xI = i; 
	break;
      }
    }
      for (int i=0;i<x;i++){
	if (original[i] != 0){
	  mG = i; 
	  break;
	}
      }
    for (int i= x-1;i>=0;i--){
      if (original[i] != 0){
	xG = i; 
	break;
      }
    }
    if (abs(xG - mI) < abs(xI - mG) ){
      threshold = float(float((abs(xG+mI)/2))*(pow(10,-6))); 
			index = (abs(xG+mI)/2);
    }
    else{
      threshold = float(float((abs(xI+mG)/2))*(pow(10,-6)));
      index = (abs(xI+mG)/2);
    }
  }
  
infile.open("../L4.txt");  
ofstream farfile;
 ofstream frrfile;cout << threshold << endl;
farfile.open("../files/FRR.dat");
 frrfile.open("../files/FAR.dat");
 farfile << "Genuine Failed (FRR)\n";
  frrfile << "Imposter Failed (FAR)\n";
 failsub = crr;
 crr =  (float(crr)/tot)*100 ;
 cout <<"doing farfarr\n";
while(!infile.eof()){ 
  infile >> data[0] >> data[1] >> data[2] >> data[3] >> data[4] >> data[5] ;  
  score = data[5];
  if (int(data[4]) == 1){
    if (score > threshold)
      farfile << data[0]<<"\t" << data[1]<<"\t" << data[2]<<"\t" << data[3]<<"\t" << data[4]<<"\t" << data[5]<<"\n";
  } 
  else {
    if (score <= threshold)
      frrfile << data[0]<<"\t" << data[1]<<"\t" << data[2]<<"\t" << data[3]<<"\t"<< data[4]<<"\t" << data[5]<<"\n";
  } 
 }
 farfile << "FRR Cases Done\n" ;
 frrfile << "FAR Cases Done\n" ;
 cout << "done\n";
frrfile.close() ;
farfile.close();

 cout << threshold <<endl;
 float imp = float((float)imposter[index]/(float)original[0]); 
 float orig= float((float)original[index]/(float)imposter[x-1]);
 cout << imp<<endl<<orig<<endl<< fabs(imp-orig) <<endl;


 // original -- frr
 // imposter -- far
 ofstream fout ;
fout.open("../files/far_vs_frr.txt");
for(int i=0;i<x;i++)
  fout  << float(float(imposter[i])/imposter[x-1]) << " " << float(float(original[i])/original[0])<< endl;
 string sts="" ;
 sts="python create_sts.py ";
 sts =sts+ to_string(gdp);
 sts = sts +" " +to_string(0)+" "+to_string(0)+" "+to_string(0)+" ";
 sts += to_string(idp) +" " +to_string(0)+" "+to_string(0)+" "+to_string(0)+" ";
 sts += to_string(0)+" "+to_string(0)+" "+to_string(imposter[int(threshold*x)])+" "to_string(threshold)+" "+to_string("0")+" ";
 sts+= to_string(failsub)+" "+to_string(tot)+" "+to_string(original[int(threshold*x)])+" "+to_string(original[0])+" "+
   to_string(imposter[int(threshold*x)])+" "+to_string(imposter[x-1]) +" ";
 sts+= to_string(float(imposter[int(threshold*x)])/imposter[x-1]) + " " + to_string(float(original[int(threshold*x)])/original[0]) ; 
 system(&sts[0]) ; 
}

