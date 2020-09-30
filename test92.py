def minFallingPathSum(arr):
    """
    :type arr: List[List[int]]
    :rtype: int
    """
    num1=0
    num2 =0
    for i in range(len(arr)):
        if i%2==0:
            num1+= arr[i][0]
            num2 += arr[i][1]
        else:
            num1 += arr[i][1]
            num2 += arr[i][0]
    return min(num1,num2)

