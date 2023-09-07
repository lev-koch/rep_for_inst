#для 3
arr=[1,0,2,3,0,4,5,0]

#1
def task_1(nums,queries):
    answers=[]
    for i in queries:
        nums[i[1]] += i[0]
        s=0
        for k in nums:
            if k%2==0:
                s+=k
        answers.append(s)
    return answers

#2
def task_2(nums, k):
    nums2=nums[0:k]
    nums=nums[k:]
    nums=nums+nums2
    return nums

#3
def task_3():
    global arr
    arr2=[]
    for i in arr:
        if len(arr)==len(arr2):
            break
        if i!=0:
            arr2.append(i)
        if i==0:
            arr2.append(i)
            arr2.append(0)
    arr=arr2

#4
def task_4(s,c):
    symb_nums=[]
    for i in range(len(s)):
        if s[i]==c:
            symb_nums.append(i)
    answer=[]
    for i in range(len(s)):
        if s[i]==c:
            answer.append(0)
        else:
            min=len(s)
            for k in symb_nums:
                if abs(k-i)<min:
                    min=abs(k-i)
            answer.append(min)
    return answer

#5
def task_5(n):
    n=bin(n)
    n=n[2:]
    n2=""
    for i in n:
        if i=="1":
            n2+="0"
        if i=="0":
            n2+="1"
    n=int(n2,2)
    return(n)



nums = [1,2,3,4]
queries = [[1,0],[-3,1],[-4,0],[2,3]]
print(task_1(nums, queries))
print(task_2([1,2,3,4,5,6,7],3))
task_3()
print(arr)
print(task_4("loveleetcode","e"))
print(task_5(5))