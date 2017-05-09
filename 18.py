'''
实现一个函数，检查二叉树是否平衡，
平衡的定义如下，对于树中的任意一个结点，其两颗子树的高度差不超过1。
给定指向树根结点的指针TreeNode* root，请返回一个bool，代表这棵树是否平衡。
'''


# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x,left=None,right=None):
         self.val = x
         self.left = left
         self.right = right




class Balance:
    def isBalance(self, root):
        # write code here
        if root == None:
            return True
        if root.left == None and root.right == None:
            return True
        return self.isBalance(root.left) and self.isBalance(root.right) and abs(
            self.depth(root.left) - self.depth(root.right)) <= 1

    def depth(self, root):
        if root == None:
            return 0
        else:
            return 1 + max(self.depth(root.left), self.depth(root.right))

if __name__ == '__main__':
    root = TreeNode('D', TreeNode('B', TreeNode('A'), TreeNode('C')), TreeNode('E', right=TreeNode('G', TreeNode('F'))))
    b=Balance()
    print(b.treeDepth(root))
    print(b.isBalance(root))