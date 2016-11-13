"""
Illustrating search in binary tree
TIME COMPLEXITY: O(n)
"""

"""Initialising the tree node having the data part left node and right node"""
class TreeNode(object):
    def __init__(self, value=None):
        self.data = value
        self.right = None
        self.left = None

"""Initialising Tree Data structure"""
class Tree(object):
    def __init__(self, head = None):
        self.root = head

    """
    Search function searches for the element to be searched for
    Args:
        value: value to be searched for
    Returns:
        True/False if element is found or not
    """
    def search(self, value):
        return self.searchHelper(self.root, value)

    """
    Helper function for search function which is called recursively
    to search for the value in the tree
    Args:
        root: root value of the tree
        value: value to be searched for
    Returns:
        True/False if element is found or not
    """
    def searchHelper(self, root, value):
        if not root:
            return

        if root.data == value:
            return True
        else:
            return self.searchHelper(root.right, value) or self.searchHelper(root.left, value)

        return False

"""initialising tree nodes"""
node1 = TreeNode('a')
node2 = TreeNode('b')
node3 = TreeNode('c')
node4 = TreeNode('d')
node5 = TreeNode('e')
node6 = TreeNode('f')
node7 = TreeNode('g')

"""assigning child nodes to the tree nodes"""
node1.left = node2
node1.right = node3

node2.left = node4
node2.right = node5

node3.right = node6

node5.left = node7

tree = Tree(node1)

"""search for the value in the tree"""
print tree.search('p')