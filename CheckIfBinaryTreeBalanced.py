"""
Illustrating wether a binary tree is balanced or not
A binary tree is balanced if the max height difference of the children
of a node is not greater than one. Since we have to traverse all the
nodes so the time complexity is O(n)

Time Complexity : O(n)
Space Complexity : O(1)
"""


class TreeNode:

    def __init__(self, value = None):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:

    def __init__(self, root = None):
        self.root = root

    def insert(self, node):
        return self.insertHelper(node, self.root)

    def insertHelper(self, node, root):
        if node.value > root.value:
            if not root.right:
                root.right = node
            else:
                return self.insertHelper(node, root.right)
        else:
            if not root.left:
                root.left = node
            else:
                return self.insertHelper(node, root.left)

    def isBalanced(self):
        return self.isBalancedHelper(self.root)

    def isBalancedHelper(self, root):
        if root is None:
            return 0

        lHeight = self.isBalancedHelper(root.left)
        rHeight = self.isBalancedHelper(root.right)

        if max(lHeight, rHeight) - min(lHeight, rHeight) > 1:
            return False

        return max(lHeight, rHeight) + 1



"""initialising tree nodes"""
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)

tree = BinaryTree(node4)

tree.insert(node2)
tree.insert(node7)
tree.insert(node6)
tree.insert(node3)
tree.insert(node5)
tree.insert(node1)

if tree.isBalanced():
    print "Tree is balanced"
else:
    print "Tree is not balanced"