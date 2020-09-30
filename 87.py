def removeDuplicates( s, k):
    """
    :type s: str
    :type k: int
    :rtype: str
    """
    stacktime = []
    stack = []

    cnt = 0
    curword = ''
    size = len(s)

    index = 0
    while index < size:
        if not curword:
            cnt += 1
            curword = s[index]
            index += 1
            continue
        if s[index] == curword:
            cnt += 1
            if cnt == k:
                if stack:
                    curword = stack.pop()
                    cnt = stacktime.pop()
                else:
                    curword = ''
                    cnt = 0
            index += 1
        else:
            stack.append(curword)
            stacktime.append(cnt)
            curword = s[index]
            cnt = 1
            index += 1
    if curword:
        stack.append(curword)
        stacktime.append(cnt)
    if not stack:
        return ''
    else:
        res = ''
        for i in range(len(stack)):
            res = res+stack[i]*stacktime[i]
        return res


s = "pbbcggttciiippooaais"
k = 2

print(removeDuplicates(s,k))