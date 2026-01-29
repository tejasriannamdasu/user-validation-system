name=input("Full Name: ")
email=input("Email: ")
number=input("Mobile: ")
age=int(input("Age: "))
flag=0
#for full name verification
if  name.count(" ")>=1 and name[0]!=" " and name[len(name)-1]!=" " :
   flag=flag+1
#for email ID verification
count1=email.count("@")
count2=email.count(".")
if count1==1 and count2==1 and email[0]!='@':
   flag = flag+1
#for mobile number verification
if len(number)==10 and number[0]!="0" and   number.isdigit():
   flag = flag+1
#for age verification
if age>=18 and age <=60:
   flag=flag+1
if flag==4:
   print(" User Profile is VALID")
else:
   print(" User Profile is INVALID")