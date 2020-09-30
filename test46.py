def minAvailableDuration(slots1, slots2, duration):
    """
    :type slots1: List[List[int]]
    :type slots2: List[List[int]]
    :type duration: int
    :rtype: List[int]
    """
    size1 = len(slots1)
    size2 = len(slots2)
    index1 = 0
    index2 = 0
    slots1.sort(key = lambda x:x[0])
    slots2.sort(key = lambda x:x[0])


    while index1<size1 and index2<size2:
        s1,e1 = slots1[index1]
        s2,e2 = slots2[index2]
        if e1<=s2:
            index1+=1
        elif e2<=s1:
            index2+=1
        else:
            s12 = max(s1,s2)
            e12 = min(e1,e2)
            if e12-s12>=duration:
                return[s12,s12+duration]
            if s1>s2:
                index2+=1
            else:
                index1+=1
    return []



slots1 = [[216397070,363167701],[98730764,158208909],[441003187,466254040],[558239978,678368334],[683942980,717766451]]
slots2 = [[50490609,222653186],[512711631,670791418],[730229023,802410205],[812553104,891266775],[230032010,399152578]]
duration = 456085
print(minAvailableDuration(slots1,slots2,duration))