def isMagic( target):
    """
    :type target: List[int]
    :rtype: bool
    """

    size =len(target)
    if size==1:
        return True
    num1 =[]
    num2 =[]
    for i in range(0,size):
        if i%2==0:
            num1.append(i+1)
        else:
            num2.append(i+1)
    num= num2+num1
    k = 0
    for i in range(size):
        if target[i]!=num[i]:
            k=i
            break
    else:
        k=size-1
    if k==0:
        return False
    newnum = num[:k]
    num = num[k:]
    target = target[k:]
    def ischange(num,target):
        if not num:
            return True
        curnum1 = []
        curnum2 = []
        for i in range(0, len(num)):
            if i %2 != 0:
                curnum1.append(num[i])
            else:
                curnum2.append(num[i])
        curnum = curnum1 + curnum2
        if target[:k]==curnum[:k]:
            return ischange(curnum[k:],target[k:])
        else:
            return False
    return ischange(num,target)


target = [2,1]
print(isMagic(target))






