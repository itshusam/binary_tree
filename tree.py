class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursive(node.right, value)

    def inorder_traversal(self):
        return self._inorder_traversal(self.root)

    def _inorder_traversal(self, node):
        if node is None:
            return []
        return (self._inorder_traversal(node.left) + 
                [node.value] + 
                self._inorder_traversal(node.right))

    def preorder_traversal(self):
        return self._preorder_traversal(self.root)

    def _preorder_traversal(self, node):
        if node is None:
            return []
        return ([node.value] + 
                self._preorder_traversal(node.left) + 
                self._preorder_traversal(node.right))

    def postorder_traversal(self):
        return self._postorder_traversal(self.root)

    def _postorder_traversal(self, node):
        if node is None:
            return []
        return (self._postorder_traversal(node.left) + 
                self._postorder_traversal(node.right) + 
                [node.value])

values = [50, 30, 70, 40, 20, 60, 80]

bst = BinarySearchTree()

for value in values:
    bst.insert(value)

inorder_result = bst.inorder_traversal()
preorder_result = bst.preorder_traversal()
postorder_result = bst.postorder_traversal()
print("In-order Traversal:", inorder_result)
print("Pre-order Traversal:", preorder_result)
print("Post-order Traversal:", postorder_result)
