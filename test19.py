def wiggleSort(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """

    size = len(nums)

    def quicksort(left, right):
        if left == right:
            return

        priot = left
        curleft = left + 1
        curright = right
        while True:
            while curleft < curright:
                if nums[curleft] > nums[priot]:
                    break
                curleft += 1


            while curright > curleft:
                if nums[curright] <= nums[priot]:
                    break
                curright -= 1
            nums[curleft], nums[curright] = nums[curright], nums[curleft]
            if curleft == curright:
                if nums[curleft]>nums[priot]:
                    curleft-=1
                break
        nums[priot], nums[curleft] = nums[curleft], nums[priot]
        priot = curleft

        quicksort(left, priot)
        quicksort(priot + 1, right)

    quicksort(0, size - 1)

    index = size-1
    for i in range(1,size//2,2):
        nums[i],nums[index] = nums[index],nums[i]
        index-=1


    return nums

nums = [3,5,2,1,6,4]
print(wiggleSort(nums))
