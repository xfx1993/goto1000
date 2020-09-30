def reverseKGroup( head, k):
    """
    :type head: ListNode
    :type k: int
    :rtype: ListNode
    """
    curnode = head

    def reversenode(curhead):
        tail = head
        front = head.next
        tail.next = None
        while front:
            curnode = front
            front = front.next
            curnode.next = tail
            tail = curnode
        return tail, head

    def dfs(curnode):
        cur = curnode
        count = 1
        precur = cur
        while cur:
            precur = cur
            cur = cur.next
            if not cur:
                break
            count += 1
            if count == k:
                break
        if count < k:
            return curnode, precur
        nextnode = cur.next
        cur.next = None

        h, t = reversenode(curnode)
        if nextnode:
            h1, t1 = dfs(nextnode)
            t.next = h1
            return h, t1
        else:
            return h, t

    newhead, newtail = dfs(curnode)
    return newhead