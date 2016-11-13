"""
Illustrating various strategies for Tree Traversal
-preOrderTraversal
-inOrderTraversal
-postOrderTraversal
-levelOrderTraversal
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
    traversing in preOrderTraversal which involves following order
    <root> <left> <right>
    """
    def preOrderTraversal(self, root):
        if not root:
            return
        print root.data
        self.preOrderTraversal(root.left)
        self.preOrderTraversal(root.right)

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
        traversing in postOrderTraversal which involves following order
        <left> <right> <root>
    """
    def postOrderTraversal(self, root):
        if not root:
            return
        self.postOrderTraversal(root.left)
        self.postOrderTraversal(root.right)
        print root.data

    """
        traversing in levelOrderTraversal which involves
        travering the tree in linear order ie starting from left to right
        all the way to all levels of the tree
    """
    def levelOrderTraversal(self, root):
        if not root:
            return
        queue = []
        while root:
            print root.data
            if root.left:
                queue.append(root.left)
            if root.right:
                queue.append(root.right)
            if queue:
                root = queue[0]
                queue.remove(queue[0])
            else:
                break

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

print "Pre Order Tree Traversal is: "
tree.preOrderTraversal(node1)

print "In Order Tree Traversal is: "
tree.inOrderTraversal(node1)

print "Post Order Tree Traversal is: "
tree.postOrderTraversal(node1)

print "Level Order Tree Traversal is"
tree.levelOrderTraversal(node1)