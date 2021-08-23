def get_memory_score(input_nums):
    b=[]
    t=0
    for i in range(len(input_nums)):
        if input_nums[i] in b:
            t=t+1
        elif(len(b)>4):
            b.pop(0)
            b.append(input_nums[i])
        else:
            b.append(input_nums[i])    
    return t
        

input_nums = [3, 4, 1, 6, 3, 3, 9, 0, 0, 0]
mylist=[]
count=0
for i in range(len(input_nums)):
        if(str(input_nums[i]).isdigit() and input_nums[i]<10):
            continue
        else:
            count=1
            mylist.append(input_nums[i])
if(count==1):    
    print("Please enter a valid input list.")
    print("Invalid inputs detected : ",mylist)
else:
    print("Score :", get_memory_score(input_nums))