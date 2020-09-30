class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

head = ListNode(4)
node1 = ListNode(2)
node2 = ListNode(1)
node3 =ListNode(3)

head.next= node1
node1.next = node2

node2.next = node3









def insertionSortList( head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        newhead = ListNode(float('-inf'))
        newhead.next = head
        pre = dict()
        curnode = head
        prenode = newhead
        while curnode:
            if curnode.val >= prenode.val:
                pre[curnode] = prenode
                prenode = curnode
                curnode = curnode.next
            else:

                nownode = curnode
                pre[nownode]=prenode
                node = curnode
                curnode = curnode.next
                prenode.next = curnode

                while pre[nownode].val > node.val:
                    nownode = pre[nownode]
                curpre = pre[nownode]
                curpre.next = node
                node.next = nownode
                pre[node] = curpre
                pre[nownode] = node

        return newhead.next


print(insertionSortList(head))