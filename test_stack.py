class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def preorderTraversal(self, root):
        ret = []
        stack = [(root, False)]
        temp = stack[-1]
        print(temp)
        while stack:
            node = stack.pop()
            if node:
                ret.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return ret

r1 = TreeNode(4)
r2 = TreeNode(2)
# r3 = TreeNode(6)
# r4 = TreeNode(1)
# r5  =TreeNode(3)
# r6 = TreeNode(5)
# r7 = TreeNode(7)


r1.left = r2
# r1.right = r3
# r2.left = r4
# r2.right = r5
# r3.left = r6
# r3.right = r7

a = Solution().preorderTraversal(r1)
print(a)