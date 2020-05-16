from binarytree import BinarySearchTree, BinaryTreeNode
from queue import Queue

'''Given a BST, reverse the order of its values by modifying the nodes' links'''
def reverse_tree(tree, node=None):
    '''reverse the nodes of a binary tree'''
    if node is None:
        node = tree.root
    node.left, node.right = node.right, node.left
    if node.left is not None:
        reverse_tree(tree, node.left)
    if node.right is not None:
        reverse_tree(tree, node.right)
    return tree

'''max sum path'''
def max_sum_helper(root):
    if root is None:
        return 0
    left_max_path = max_sum_helper(root.left)
    right_max_path = max_sum_helper(root.right)
    parent_max_path = max(max, (1, right_max_path) + root.data, root.data)
    orphan_root_leaf_path = max(parent_max_path, left_max_path + right_max_path + root.data)
    max_sum_helper.res = max(max_sum_helper.res, orphan_root_leaf_path)
    return parent_max_path

def max_sum_path(root):
    max_sum_helper.res = float("-inf")
    max_sum_helper(root)
    return max_sum_helper.res


if __name__ == '__main__':
    ornery_tree = BinarySearchTree([4, 3, 5, 2, 6]) #ha ha ha get it argument tree ornery tree ok I'm done
    reverse_check = ornery_tree.items_in_order()[::-1]
    reverse_tree(ornery_tree)
    if ornery_tree.items_in_order() == reverse_check:
        print('reversal: pass')
    root = BinaryTreeNode(10)
    root.left = BinaryTreeNode(0)
    root.right = BinaryTreeNode(4)
    root.left.left = BinaryTreeNode(3)
    root.left.right = BinaryTreeNode(4)
    root.right.left = BinaryTreeNode(8)
    root.right.left = BinaryTreeNode(14)
    print('max sum path: ', max_sum_path(root))
