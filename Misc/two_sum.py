nums = [3,2,3]
value = 6

def two_sum(numArray,target):
    sumIndexArray = []
    for i in range(0, len(nums)-1):
        print('i',i)
        for j in range(i+1,len(nums)):
            print('j',j)
            if nums[i] + nums[j] == target:
                sumIndexArray.insert(0,i)
                sumIndexArray.insert(1,j)
    return sumIndexArray      

print(two_sum(nums,value))
