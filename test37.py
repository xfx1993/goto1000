def areSentencesSimilarTwo(self, words1, words2, pairs):
    """
    :type words1: List[str]
    :type words2: List[str]
    :type pairs: List[List[str]]
    :rtype: bool
    """
    size1 = len(words1)
    size2 = len(words2)
    if size1 != size2:
        return False

    father = dict()

    def findroot(node):
        while father[node] != node:
            father[node] = father[father[node]]
            node = father[node]
        return node

    for w1, w2 in pairs:
        if w1 not in father:
            father[w1] = w1
        if w2 not in father:
            father[w2] = w2
        w1_root = findroot(w1)
        w2_root = findroot(w2)
        father[w2_root] = w1_root
        father[w2] = w1_root

    for i in range(size1):
        if words1[i]==words2[i]:
            continue
        else:
            if words1 not in father or words2 not in father:
                return False
            else:
                wroot1 = findroot(words1)
                wroot2 = findroot(words2)
                if wroot1!=wroot2:
                    return False
    return True

print()
