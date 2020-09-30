

def myquicksort(nums):


    size=len(nums)


    def partition(left,right):
        pvoit = nums[left]

        j= left
        for i in range(left+1,right+1):
            if nums[i]<pvoit:
                j=j+1
                nums[j],nums[i] = nums[i],nums[j]
        nums[j],nums[left] = nums[left],nums[j]
        return j

    def quicksort(left,right):
        if left>=right:
            return
        mid = partition(left,right)
        quicksort(left,mid-1)
        quicksort(mid+1,right)
    quicksort(0,size-1)
    return nums


import random
import time
nums = []
for i in range(10000):
    nums.append(random.randint(1,1000))

print(nums)
# time1 = time.clock()
# print(myquicksort(nums))
# time2 = time.clock()
# print(time2-time1)

time1 = time.clock()
nums.sort()
time2 = time.clock()
print(time2-time1)
