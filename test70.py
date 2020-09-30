class LineTree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.sumrange = 0


class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

        def create_linetree(left, right):
            if left==right:
                node = LineTree([left, right])
                node.sumrange = nums[left]
                return node
            else:
                mid = (left + right) // 2
                curnode = LineTree([left, right])
                curnode.left = create_linetree( left, mid)
                curnode.right = create_linetree( mid + 1, right)
                curnode.sumrange = curnode.left.sumrange+curnode.right.sumrange
                return curnode
        self.head = create_linetree( 0, len(self.nums) - 1)
    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: None
        """
        old_val = self.nums[i]
        self.nums[i] = val
        curnode = self.head

        def update(pos, curnode):
            if not curnode:
                return
            l, r = curnode.val
            if pos == l and pos == r:
                curnode.sumrange = val
                return
            if pos <= (l + r) // 2:
                update(pos, curnode.left)
            else:
                update(pos, curnode.right)
            curnode.sumrange = curnode.sumrange - old_val + val
        update(i, curnode)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        curnode = self.head

        def get_sumrange(i, j, curnode):
            if not curnode:
                return 0
            l, r = curnode.val

            if i == l and j == r:
                return curnode.sumrange
            mid = (l + r) // 2
            if j <= mid:
                return get_sumrange(i, j, curnode.left)
            elif i > mid:
                return get_sumrange(i, j, curnode.right)
            else:
                return get_sumrange(i, mid, curnode.left) + get_sumrange(mid + 1, j, curnode.right)

        return get_sumrange(i, j, curnode)



obj = NumArray([0,9,5,7,3])
print(obj.sumRange(4,4))
