def numberOfSubstrings(s):
    """
    :type s: str
    :rtype: int
    """
    size = len(s)
    used = dict()
    used['a']=0
    used['b']=0
    used['c']=0
    res=0
    count = 3
    index = 0
    for i in range(len(s)):
        while count>0 and index<size:
            if used[s[index]]==0:
                count-=1
                used[s[index]]+=1
            else:
                used[s[index]]+=1
            index+=1
        if count==0:
            res=res+1+size-index
        if used[s[i]]-1==0:
            count+=1
            used[s[i]]-=1
        else:
            used[s[i]] -= 1
    return res

s = "aaacb"
print(numberOfSubstrings(s))



