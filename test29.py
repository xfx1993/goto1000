# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def str2tree(s):
    """
    :type s: str
    :rtype: TreeNode
    """

    def creatTree(s):
        if not s:
            return None
        index = 0
        headnum = 0
        for i, v in enumerate(s):
            if v == '(':
                index = i
                break
        else:
            headnum = int(s)
            return TreeNode(headnum)
        headnum = int(s[:index])
        curnode = TreeNode(headnum)
        left = 0
        right = 0
        bre = 0
        for i in range(index, len(s)):
            if s[i] == '(':
                left += 1
            elif s[i] == ')':
                right += 1
            if left == right:
                bre = i
                break
        leftnode = creatTree(s[index + 1:bre])
        rightnode = None
        if s[bre + 1:]:
            rightnode = creatTree(s[bre + 2:len(s) - 1])
        curnode.left = leftnode
        curnode.right = rightnode
        return curnode

    return creatTree(s)

s = "4(2(3)(1))(6(5))"

print(str2tree(s))

