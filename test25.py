def breakfastNumber( staple, drinks, x):
    """
    :type staple: List[int]
    :type drinks: List[int]
    :type x: int
    :rtype: int
    """
    staple.sort()
    drinks.sort()

    count = 0
    row = len(staple)
    col = len(drinks)
    for i in range(row):
        if staple[i]>x:
            break
        target = x-staple[i]
        left = 0
        right = col
        while left<right:
            mid =(left+right)//2
            if drinks[mid]<=target:
                left = mid+1
            else:
                right =mid
        count+=left
    return count


staple = [2,1,1]
drinks = [8,9,5,1]
x = 9

print(breakfastNumber(staple,drinks,x))
