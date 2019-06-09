val=input("Enter your value: ") 
print("The value :",val)
ctr=1
i=0
while  i<len(val):
    if ord(val[i])>=48 and ord(val[i])<=57:
        i=i+1
    else :
        ctr=0
        i=len(val)+1
if ctr==1:
    print("True")
else :
    print("False")
    