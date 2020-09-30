def smallestStringWithSwaps(s, pairs):
    """
    :type s: str
    :type pairs: List[List[int]]
    :rtype: str
    """
    size = len(s)

    father = [i for i in range(size)]

    def findroot(node):
        while father[node]!=node:
            father[node]=father[father[node]]
            node=father[node]
        return node

    for node1,node2 in pairs:
        node1_root = findroot(node1)
        node2_root = findroot(node2)
        father[node2_root] = node1_root
    dic =dict()
    news = ['' for i in range(size)]

    for i in range(size):
        curfather = findroot(i)
        if curfather not in dic:
            dic[curfather]=[i]
        else:
            dic[curfather].append(i)



    for k,values in dic.items():
        values.sort()
        words =[]
        for v in values:
            words.append(s[v])
        words.sort()
        for i,w in enumerate(words):
            news[values[i]]=w

    return ''.join(news)

s = "dcab"
pairs = [[0,3],[1,2],[0,2]]

print(smallestStringWithSwaps(s,pairs))
