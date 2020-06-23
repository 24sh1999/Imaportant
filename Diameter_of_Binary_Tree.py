class Solution:
    
    def long_distance(self, root):
        if root == None:
            return 0
        a = self.long_distance(root.left)
        b = self.long_distance(root.right)
        self.max = max(a + b, self.max)
        return max(a, b) + 1
        
    

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.max = 0
        self.long_distance(root)
        return self.max
