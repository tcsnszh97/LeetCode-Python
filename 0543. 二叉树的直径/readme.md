# 0543. 二叉树的直径

本题要求计算直径，很明显这道题是要考察深度遍历。

深度遍历最简单的实现办法就是递归。

值得一提的是，我们不需要在调用函数的时候判断结点的子结点是否存在，而是在函数调用后再去判断结点是否为None。

``` python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.max = 0

        def depth(root: TreeNode):
            if not root:
                return 0
            left_depth = depth(root.left)
            right_depth =  depth(root.right)
            self.max = max(self.max, left_depth + right_depth)
            return max(left_depth, right_depth)+1

        depth(root)
        return self.max
```
