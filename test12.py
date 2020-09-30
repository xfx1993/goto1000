
def pyramidTransition(bottom, allowed):
    """
    :type bottom: str
    :type allowed: List[str]
    :rtype: bool
    """
    help = dict()
    for word in allowed:
        front = word[:2]
        if front not in help:
            help[front]=[word[2]]
        else:
            help[front].append(word[2])

    def dfs(nextf,size,cen,nextflo,stack):
        if cen==size:
            nextflo.append(''.join(stack[:]))
            return

        for w in nextf[cen]:
            stack.append(w)
            dfs(nextf,size,cen+1,nextflo,stack)
            stack.pop()


    def getnextcen(curbottom):
        nextf = []
        for i,w in enumerate(curbottom):
            if i==0:
                continue
            curfront = curbottom[i-1]+curbottom[i]
            if curfront not in help:
                return []
            curfather = help[curfront]
            nextf.append(curfather)
        size = len(nextf)
        nextflo = []
        stack = []
        dfs(nextf,size,0,nextflo,stack)
        return nextflo


    bottoms = [bottom]
    flag = [False]
    dic = dict()
    def istower(bottoms):
        if not bottoms:
            return False
        if tuple(bottoms) in dic:
            return dic[tuple(bottoms)]
        cur = False
        for curbottom in bottoms:
            if len(curbottom)==1:
                return True
            nextbottoms = getnextcen(curbottom)
            cur = cur or istower(nextbottoms)
        dic[tuple(bottoms)]=cur
        return cur

    istower(bottoms)
    return flag[0]


bottom = "AABA"
allowed = ["AAA", "AAB", "ABA", "ABB",'BAA','BBA',"BAC"]
print(pyramidTransition(bottom,allowed))


