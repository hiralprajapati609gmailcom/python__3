s=input("Enter Sring : ")

a1=0
nm=0
cp=0
sm=0
sp=0

for i in s:
     if i.isalpha():
         a1=a1+1
     elif i.isnumeric():
         nm=nm+1
     elif i.isspace():
         sp=sp+1
     if i.islower():
         sm=sm+1
     elif i.isupper():
         cp=cp+1
 print("Total Alphabets : ",a1)
 print("Total Numerical : ",nm)
 print("Total Capital : ",cp)
 print("Total Small : ",sm)
 print("Total Space: ",sp)
