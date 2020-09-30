# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

head = ListNode(1)
node1 = ListNode(2)
node2 = ListNode(3)
node3 = ListNode(4)
node4 = ListNode(5)
head.next = node1
node1.next = node2
node2.next = node3
node3.next = node4

def reverseKGroup( head, k):
    """
    :type head: ListNode
    :type k: int
    :rtype: ListNode
    """
    curnode = head


    def reversenode(curhead):
        tail = curhead
        front = head.next
        tail.next=None
        while front:
            curnode = front
            front=front.next
            curnode.next = tail
            tail = curnode
        return tail,head

    def dfs(curnode):
        cur = curnode
        count=1
        precur = cur
        while cur:
            precur = cur
            cur=cur.next
            count+=1
            if count==k:
                break
        if count<k or not cur:
            return curnode,precur

        nextnode = cur.next
        cur.next = None

        h,t = reversenode(curnode)
        if nextnode:
            h1,t1 = dfs(nextnode)
            t.next=h1
            return h,t1
        else:
            return h,t

    newhead,newtail = dfs(curnode)
    return newhead



print(reverseKGroup(head,2))


