#!/usr/bin/python
#-*- coding:utf-8 -*-
############################
# File Name: tree.py
# Author: Neablister
# Mail: 943272448@qq.com
# Created Time: 2019-02-12 22:54:46
############################

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def construct_tree():
    """
    Construct the tree
       5
      / \
     3   6
    / \  /
    2  4 7
    """
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(8)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(7)
    return root

def level_traversal(root):
    """
    二叉树层次遍历
    构造一个队列queue(type = list, 元素为TreeNode)和index作为索引
    result返回每个节点的value
    """
    if root is None:
        return []
    index = 0
    queue = []
    result = []
    queue.append(root)
    while len(queue) > index:
        tmp = queue[index]
        result.append(tmp.val)
        index += 1
        if tmp.left is not None:
            queue.append(tmp.left)
        if tmp.right is not None:
            queue.append(tmp.right)
    return result

def inorder_traversal(tree_node, queue = []):
    """
    二叉树中序遍历递归实现
    """
    if tree_node is not None:
        inorder_traversal(tree_node.left, queue)
        queue.append(tree_node.val)
        inorder_traversal(tree_node.right, queue)
    return queue

def preorder_traversal(tree_node, queue = []):
    """
    二叉树前序遍历递归实现
    """
    if tree_node is not None:
        queue.append(tree_node.val)
        preorder_traversal(tree_node.left, queue)
        preorder_traversal(tree_node.right, queue)
    return queue

def postorder_traversal(tree_node, queue = []):
    """
    二叉树后序遍历递归实现
    """
    if tree_node is not None:
        postorder_traversal(tree_node.left, queue)
        postorder_traversal(tree_node.right, queue)
        queue.append(tree_node.val)
    return queue

def max_depth(tree_node):
    """
    计算二叉树的最大深度递归实现
    思路: 分别求左右子树的高度, 哪个大就+1
    """
    if tree_node is not None:
        return max(max_depth(tree_node.left) + 1, max_depth(tree_node.right) + 1)
    else:
        return 0

if __name__ == "__main__":
    root = construct_tree()
    print(level_traversal(root))
    print(inorder_traversal(root))
    print(preorder_traversal(root))
    print(postorder_traversal(root))
    print(max_depth(root))
