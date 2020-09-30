def flipLights( n, m):
    """
    :type n: int
    :type m: int
    :rtype: int
    """
    if m==0:
        return 1
    if n ==1 and m==0:
        return 1
    elif n==1 and m>=1:
        return 2
    num1 = int('1'*n,2)

    change1=num1
    change2=0
    change3 =0
    if n%2==0:
        change2 = int('01'*(n//2),2)
        change3 = int('10'*(n//2),2)
    else:
        change2 =  int('01'*(n//2)+'0',2)
        change3 =  int('10'*(n//2)+'1',2)
    change4 =['0']*n
    for i in range(1000):
        if 3*i+1>n:
            break
        change4[3*i]='1'
    change4 = int(''.join(change4),2)

    used =dict()
    count=[0]
    nodes = [num1]
    change = [change1,change2,change3,change4]
    cen=0
    while nodes:
        if cen==m:
            return len(nodes)
        cen+=1

        curnode=[]
        for node in nodes:
            for c in change:
                cur = node^c
                if cur not in curnode:
                    curnode.append(cur)
        nodes=curnode

n=100
m=3

print(flipLights(n,m))





