# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if len(pre) == 0:
            return None
        elif len(pre) == 1:
            return TreeNode(pre[0])
        root = TreeNode(pre[0])
        root_idx = tin.index(pre[0])
        root.left = self.reConstructBinaryTree(pre[1:root_idx+1],tin[:root_idx])
        root.right = self.reConstructBinaryTree(pre[root_idx+1:],tin[root_idx+1:])
        return root