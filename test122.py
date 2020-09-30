def paintingPlan( n, k):
    """
    :type n: int
    :type k: int
    :rtype: int
    """
    if k==n*n:
        return 1
    count=0
    def get(num):
        num1 =1
        for i in range(1,num+1):
            num1 =num1*i
        num2 =1
        for j in range(n,n-num,-1):
            num2=num2*j
        return num2//num1

    for i in range(0,n+1):
        for j in range(0,n+1):
           if i*n+j*n-i*j==k:
                if i==0 and j!=0:
                    count += get(j)
                elif i!=0 and j==0:
                    count+=get(i)
                else:
                    count += get(i)*get(j)
    return count

print(paintingPlan(4,13))