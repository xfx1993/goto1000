# class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        target = int(target*10)
        size =0
        import heapq
        heap = []
        stack =[]
        curnode =root
        while curnode or stack:
            while curnode:
                stack.append(curnode)
                curnode = curnode.left
            curnode = stack.pop()
            val = curnode.val*10
            if size<k:
                heapq.heappush([-abs(val-target),curnode.val],key=lambda x)
            else:
                if -abs(val-target)<heap[0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap,[-abs(val-target),curnode.val])
                else:
                    break

            curnode = curnode.right

        return [x[1] for x in heap]

