"""
Illustrating inserting in binary search tree
TIME COMPLEXITY average case: O(log n)
TIME COMPLEXITY worst case: O(n)
"""

"""Initialising the tree node having the data part left node and right node"""
class TreeNode(object):
    def __init__(self, value=None):
        self.data = value
        self.right = None
        self.left = None

class BinarySearchTree(object):
    def __init__(self, root=None):
        self.root = root

    """
    insert function for the tree
    Args:
        node: new node to be inserted
    """
    def insert(self, node):
        if not self.root:
            self.root = node
            return
        else:
            root = self.root
            self.insertHelper(root, node)

    """
    insert helper function
    Args:
        root: root node for the binary search tree
        node: node to be inserted
    """
    def insertHelper(self, root, node):
        if root.data > node.data:
            if not root.left:
                root.left = node
            else:
                self.insertHelper(root.left, node)
        else:
            if not root.right:
                root.right = node
            else:
                self.insertHelper(root.right, node)

    """
        traversing in inOrderTraversal which involves following order
        <left> <root> <right>
    """
    def inOrderTraversal(self, root):
        if not root:
            return
        self.inOrderTraversal(root.left)
        print root.data
        self.inOrderTraversal(root.right)

    """
    Search input value in the tree
    Args:
        value: value to be searched for
    """
    def search(self, value):
        return self.searchHelper(self.root, value)

    """
    search helper function, search the value in the tree through recursive
    strategy
    Args:
        root: root node for the tree/subtree
        value: value to be searched for in the tree
    """
    def searchHelper(self, root, value):
        if not root:
            return False
        if int(root.data) == int(value):
            return True
        elif value < root.data:
            return self.searchHelper(root.left, value)
        else:
            return self.searchHelper(root.right, value)


"""initialising tree nodes"""
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)

tree = BinarySearchTree(node4)

tree.insert(node2)
tree.insert(node7)
tree.insert(node6)
tree.insert(node3)
tree.insert(node5)
tree.insert(node1)

tree.inOrderTraversal(node4)

print tree.search(7)