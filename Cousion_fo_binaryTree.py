## Problem Name: Cousion in Binary Tree(leetcode 30 day challenge)
## 



class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        
        
        def dfs(root, depth, parent):
            if not root or len(result) == 2:
                return
            
            if root.val == x or root.val == y:
                result.append([depth, parent])
            
            dfs(root.left, depth + 1, root)
            dfs(root.right, depth + 1, root)           
            
        result = []
        dfs(root, 0, None)


######################################################################3

######This Was my solution to the above Problem
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        xValue = []
        yValue = []
        depth = 0
        Parent = None
        
        if root == None:
            return False
        
        self.Buttom(root, x, y, 0, None, xValue, yValue)
        return xValue[0][0] == yValue[0][0] and xValue[0][1] != yValue[0][1]
    def Buttom(self, root, x, y, depth, Parent, xValue, yValue):
        if root is None:
            return None
        
        if root.val == x:
            xValue.append((depth, Parent))
        if root.val == y:
            yValue.append((depth, Parent))
            
        
        
        self.Buttom(root.left, x, y, depth + 1, root, xValue, yValue)
        self.Buttom(root.right, x, y, depth + 1, root, xValue, yValue)
