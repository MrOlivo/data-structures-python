import os
import sys

sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")))

from arboles.arbol_binario import BinaryTree

tree = BinaryTree()

items = [45, 23, 65, 2, 38, 52, 96, 7, 48]

for item in items:
    tree.insert(item)

print("INORDEN: ")
tree.inorder()
print("\nPREORDEN: ")
tree.preorder()
print("\nPOSTORDEN: ")
tree.postorder()
print("")
