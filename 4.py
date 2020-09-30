def canWin( s):
    """
    :type s: str
    :rtype: bool
    """

    def cw(s):
        if s.count('+') == 0:
            return False
        icanbring = True
        cur = False
        slist = list(s)
        flag = 0
        for i in range(1, len(slist)):
            if slist[i] == "+" and slist[i - 1] == '+':
                slist[i] = '-'
                slist[i - 1] = '-'
                cur = cur or not cw(''.join(slist))
                slist[i] = '+'
                slist[i - 1] = '+'
                flag =1
        if flag==0:
            return False

        return icanbring and cur

    return cw(s)


print(canWin("++++++"))