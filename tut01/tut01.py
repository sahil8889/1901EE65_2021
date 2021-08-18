import os
os.system("cls")
def meraki_helper(n):
    """This will detect meraki numner"""
    mylist= []
    m=n
    count=0
    while n>0:
        num=n%10
        mylist.append(num)
        n=n//10
    for i in range(len(mylist)-1):
        if(abs(mylist[i] - mylist[i+1]) != 1 ):
            print("NO," , m, "is not a meraki number")
            count=1
            return 0
    if(count==0):
        print("YES," , m, "is a meraki number")

    
input = [12, 14, 56, 78, 98, 54, 678, 134, 789, 0, 7, 5, 123, 45, 76345, 987654321]
t=0
for i in range(len(input)):
    if ( meraki_helper(input[i]) == 0 ):    
        t=t+1
print("The input list contains ", len(input)-t ,"meraki numbers and ", t ,"non meraki numbers.")  
  