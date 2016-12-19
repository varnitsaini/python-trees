"""
This is to illustrate lowest common ancestor in
Binary search Tree

Runtime Complexity : O(log n)
Space Complexity : O(1)
"""


class TreeNode:

    def __init__(self, value = None):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:

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

    def findLCA(self, n1, n2):
        return self.findLCAHelper(self.root, n1, n2)

    def findLCAHelper(self, root, n1, n2):
        if root is None:
            return False

        if n1 > root.value and n2 > root.value:
            return self.findLCAHelper(root.right, n1, n2)

        if n1 < root.value and n2 < root.value:
            return self.findLCAHelper(root.left, n1, n2)

        return root.value


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

print tree.findLCA(1, 3)
