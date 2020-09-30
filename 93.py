def reversePairs( nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    ##归并算法进行逆序对计算，增加一个两倍的条件而已

    size = len(nums)
    left = 0
    right = size - 1

    count = [0]

    def mergesort(left, right):

        if left == right:
            return [nums[left]]
        mid = (left + right) // 2
        leftlist = mergesort(left, mid)
        rightlist = mergesort(mid + 1, right)

        sl = mid - left + 1
        sr = right - mid
        l = 0
        r = 0
        temp = []
        while l < sl and r < sr:
            if leftlist[l] <= rightlist[r] * 2:
                l += 1
            else:
                count[0] += sl - l 
                r += 1
        l = 0
        r = 0
        while l < sl and r < sr:
            if leftlist[l] <= rightlist[r]:
                temp.append(leftlist[l])
                l += 1
            else:
                temp.append(rightlist[r])
                r += 1
        while l < sl:
            temp.append(leftlist[l])
            l += 1
        while r < sr:
            temp.append(rightlist[r])
            r += 1

        return temp

    nums = mergesort(0, size - 1)
    return count[0]

nums = [2,4,3,5,1]
print(reversePairs(nums))