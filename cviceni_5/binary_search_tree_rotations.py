import random

class Node:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

def to_str(obj):
    if isinstance(obj, Tree):
        result = to_str(obj.root)
    elif isinstance(obj, Node):
        result = f"({obj.key} {to_str(obj.left)} {to_str(obj.right)})" 
    elif obj is None:
        result = "-"
    return result

######################################################################

def t_insert(tree, element):
    new_node = Node(element)
    index_node = tree.root
    parent_node = None

    while index_node is not None:
        parent_node = index_node
        if new_node.key < index_node.key:
            index_node = index_node.left
        elif new_node.key > index_node.key:
            index_node = index_node.right
        else:
            return
    new_node.parent = parent_node

    if parent_node is None:
        tree.root = new_node
    elif new_node.key < parent_node.key:
        parent_node.left = new_node
    else:
        parent_node.right = new_node

def t_search(tree, data):
    index_node = tree.root
    while (index_node is not None) and (index_node.key != data):
        if data < index_node.key:
            index_node = index_node.left
        else:
            index_node = index_node.right
    return index_node

def _set_left_child(parent_node, new_child_node):
    parent_node.left = new_child_node
    if new_child_node is not None:
        new_child_node.parent = parent_node

def _set_right_child(parent_node, new_child_node):
    parent_node.right = new_child_node
    if new_child_node is not None:
        new_child_node.parent = parent_node

def _set_root(tree, new_root):
    tree.root = new_root
    if new_root is not None:
        new_root.parent = None

######################################################################

def rotate_r(tree, node):
    # Insert code here
    pass

def rotate_l(tree, node):
    # Insert code here
    pass

######################################################################

foo = list(range(7))
test_tree = Tree()
for el in foo:
    t_insert(test_tree, el)

print("Test 1 expects:  (0 - (1 - (2 - (3 - (4 - (5 - (6 - (7 - -))))))))")
print(f"Test 1 gets:     {to_str(test_tree)}\n")

rotate_l(test_tree, t_search(test_tree, 0))
print("Test 2 expects:  (1 (0 - -) (2 - (3 - (4 - (5 - (6 - -))))))")
print(f"Test 2 gets:     {to_str(test_tree)}\n")

rotate_l(test_tree, t_search(test_tree, 1))
rotate_l(test_tree, t_search(test_tree, 2))
print("Test 3 expects:  (3 (2 (1 (0 - -) -) -) (4 - (5 - (6 - -))))")
print(f"Test 3 gets:     {to_str(test_tree)}\n")

rotate_r(test_tree, t_search(test_tree, 2))
rotate_l(test_tree, t_search(test_tree, 4))
print("Test 4 expects:  (3 (1 (0 - -) (2 - -)) (5 (4 - -) (6 - -)))")
print(f"Test 4 gets:     {to_str(test_tree)}\n")

