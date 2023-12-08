import math
import random

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.size = 1  # size of the subtree rooted at this node

class BinarySearchTree:
    def __init__(self, balance_constant):
        self.root = None
        self.balance_constant = balance_constant

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, root, key):
        if root is None:
            return TreeNode(key)
        
        root.size += 1  # update the size of the subtree rooted at this node

        if key < root.key:
            root.left = self._insert(root.left, key)
        elif key > root.key:
            root.right = self._insert(root.right, key)

        # Check if the subtree rooted at this node is unbalanced
        if self._is_unbalanced(root):
            root = self._balance_subtree(root)

        return root

    def _is_unbalanced(self, node):
        if node is None:
            return False

        left_size = 0 if node.left is None else node.left.size
        right_size = 0 if node.right is None else node.right.size

        return (
            left_size > self.balance_constant * node.size
            or right_size > self.balance_constant * node.size
        )

    def _balance_subtree(self, root):
        # Create a list to store the keys in sorted order
        keys = []
        self._inorder_traversal(root, keys)

        # Build a perfect balanced binary search tree using the sorted keys
        return self._build_balanced_bst(keys)

    def _inorder_traversal(self, root, keys):
        if root:
            self._inorder_traversal(root.left, keys)
            keys.append(root.key)
            self._inorder_traversal(root.right, keys)

    def _build_balanced_bst(self, keys):
        if not keys:
            return None

        mid = len(keys) // 2
        root = TreeNode(keys[mid])

        root.left = self._build_balanced_bst(keys[:mid])
        root.right = self._build_balanced_bst(keys[mid + 1:])

        # Update the size of the subtree rooted at this node
        left_size = 0 if root.left is None else root.left.size
        right_size = 0 if root.right is None else root.right.size
        root.size = left_size + right_size + 1

        return root

    def display(self):
        self._display(self.root, 0)

    def _display(self, root, level):
        if root:
            self._display(root.right, level + 1)
            print("  " * level + str(root.key))
            self._display(root.left, level + 1)

#-------------------------------------------------------------------| TEST | -------------------------------------------------------------------#

bst = BinarySearchTree(balance_constant=1)
keys = [1, 2, 3 ,4 ,5, 6, 7, 8, 9, 10]
rndKeys = [1, 2, 3 ,4 ,5, 6, 7, 8, 9, 10]
random.shuffle(rndKeys)
print (rndKeys)
for key in rndKeys:
    bst.insert(key)

# Display the balanced BST
print("Original BST:")
bst.display()
