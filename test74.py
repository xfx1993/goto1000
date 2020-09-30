class LinkNode:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.pre = None


def orderlyQueue(S, K):
    """
    :type S: str
    :type K: int
    :rtype: str
    """
    size = len(S)
    root = LinkNode("#")
    curnode = root
    for s in S:
        node = LinkNode(s)
        curnode.next = node
        node.pre = curnode
        curnode = node
    tail = curnode

    def getKnode(root,tail):
        flag = True
        while flag:
            flag = False
            head = root.next
            i = 0
            nownode = head
            while i < K and nownode:
                if nownode.next and nownode.val > nownode.next.val:
                    flag = True
                    pre = nownode.pre
                    cur = nownode
                    nownode = nownode.next
                    pre.next = nownode
                    nownode.pre = pre
                    tail.next = cur
                    cur.next = None
                    cur.pre = tail
                    tail = cur
                else:
                    nownode = nownode.next
                    i += 1

    res = ''
    while True:
        getKnode(root,tail)
        curnode = root.next
        i=0
        while i<K and curnode:
            res += curnode.val
            curnode = curnode.next
            i+=1
        if not curnode:
            break
        root.next = curnode
        curnode.pre.next=None
        curnode.pre =root
        nexttail = root
        while nexttail.next:
            nexttail = nexttail.next
        tail = nexttail

    return res


S="baacadgvdsffsafasrhrherhrgehgrhjtjtkljtsfaagukhjtynrhesfadsadehsd"

#S2="vssghedssfg"
K = 1

print(orderlyQueue(S,K))