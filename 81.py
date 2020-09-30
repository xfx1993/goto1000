def expand( S):
    """
    :type S: str
    :rtype: List[str]
    """

    choselist = []
    size = len(S)
    stack = []
    s = ''
    for i in range(size):
        if S[i] != '{' and S[i] != '}' and S[i] != ',':
            s += S[i]
        elif S[i] == '{':
            if s:
                stack.append(s)
            if stack:
                choselist.append(stack[:])
                stack = []
            s = ''
        elif S[i] == '}':
            stack.append(s)
            choselist.append(stack[:])
            s = ''
            stack = []
        elif S[i] == ',':
            stack.append(s)
            s = ''
    if s:
        stack.append(s)
    if stack:
        choselist.append(stack[:])

    length = len(choselist)

    res = []
    stack = []

    def getall(index, stack):
        if index == length:
            res.append(''.join(stack[:]))
            return
        for w in choselist[index]:
            stack.append(w)
            getall(index + 1, stack)
            stack.pop()

    getall(0, stack)
    return res


S="{a,b}c{d,e}f"
print(expand( S))