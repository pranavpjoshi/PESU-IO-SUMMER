arr=list()
n=input("Enter size: ")
n=int(n)
print("enter",n," values")
for i in range(n):
    val=n=input("Enter value: ")
    val=int(val)
    arr.append(val)
arr.sort()
print("List: ",arr) 
ele=input("Enter search value: ")
ele=int(ele) 
f=0
l=len(arr)-1
pos=-1
while f<=l:
    mid=(f+l)//2
    if ele==arr[mid]:
        pos=mid+1
        break
    elif ele>arr[mid]:
        f=mid+1
    elif ele<arr[mid]:
        l=mid-1
if pos>0:
    print("Element is at position: ",pos)
else:
    print("Element is not present in the list")