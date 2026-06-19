import random

class Node:
    tree = []
    def __init__(self, value, left_pointer=None, right_pointer=None):
        self.value = value
        self.left_pointer = left_pointer
        self.right_pointer = right_pointer
        Node.tree.append(self)

# third layer (leaf nodes)
b = Node("b")
f = Node("f")
j = Node("j")
n = Node("n")

# second layer
d = Node("d", b, f)
l = Node("l", j, n)

h = Node("h", d, l) # root node

inp = input("What value do you want to find?: ")
node = h

path = ""
not_found = False
while node.value != inp:
    if inp > node.value:
        node = node.right_pointer
        path += "1/"
    elif inp < node.value:
        node = node.left_pointer
        path += "0/"
    if node is None:
        print(f"{inp} is not in the list")
        not_found = True
        break
if not not_found:
    print(f"The value can be found at {path}")
