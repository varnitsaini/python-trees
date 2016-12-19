"""
Illustrating height of a binary tree. In this we have to traverse
all the nodes since we have to get the height of each and every node

Time Complexity : O(n)
Space Complexity : O(1)
"""


class TreeNode:

    def __init__(self, value = None):
        self.value = value
        self.right = None
        self.left = None


class BinaryTree:

    def __init__(self, node):
        self.root = node

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

    def getHeight(self):
        return self.getHeightHelper(self.root)


    def getHeightHelper(self, root):
        if root is None:
            return 0

        lHeight = self.getHeightHelper(root.left)
        rHeight = self.getHeightHelper(root.right)

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

print tree.getHeight()
