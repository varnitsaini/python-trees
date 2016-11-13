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
    Get minimum value of the tree with respect to specified node
    Args:
        node: node for which we want to find the minimum value of
    """
    def getMinimumValue(self, node):
        while node.left:
            node = node.left

        return node

    """
    Delete function
    Args:
        value: value which is to be deleted from the node
    """
    def delete(self, value):
        return self.deleteHelper(self.root, value)

    """
    Delete helper function
    Args:
        root: root node for the tree/subtree
        value: value which we want to search for
    """
    def deleteHelper(self, root, value):
        if not root:
            return root

        if value > root.data:

            """if value is greater than root data then delete from right subtree"""
            root.right = self.deleteHelper(root.right, value)
        elif value < root.data:

            """if value is smaller than root data then delete from left subtree"""
            root.left = self.deleteHelper(root.left, value)

        else:

            """check for, if node has only one child or no child"""
            if not root.right:
                temp = root.left
                root = None
                return temp

            """check for, if node has only one child or no child"""
            if not root.left:
                temp = root.right
                root = None
                return temp

            """check for node which have two child replace the node value with lowest right successor"""
            temp = self.getMinimumValue(root.right)

            root.data = temp.data

            """delete the node which is being replaced in the tree"""
            root.right = self.deleteHelper(root.right, temp.data)

        return root


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

tree.delete(3)
tree.delete(5)

tree.inOrderTraversal(node4)

