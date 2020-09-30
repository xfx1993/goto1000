def isNStraightHand( hand, W):
    """
    :type hand: List[int]
    :type W: int
    :rtype: bool
    """
    size = len(hand)
    if size % W != 0:
        return False

    handdict = dict()

    for h in hand:
        if h not in handdict:
            handdict[h] = 1
        else:
            handdict[h] += 1
    handlist = [[key, values] for key, values in handdict.items()]
    handlist.sort(key=lambda x: x[0])
    index = 0
    size = len(handlist)
    while index < size:
        if handlist[index][1] == 0:
            index += 1
            continue
        nextindex = index
        curcount = handlist[index][1]
        for i in range(0, W):
            if index + i >= size:
                return False
            if handlist[index+i][0]-handlist[index][0]!=i:
                return False
            if handlist[index + i][1] >= curcount:
                handlist[index + i][1] -= curcount
                if handlist[index + i][1] == 0:
                    nextindex = index + i
            else:
                return False
        index = nextindex
    return True
hand = [1,2,3,6,2,3,4,7,8]
W = 3

print(isNStraightHand(hand,W))
