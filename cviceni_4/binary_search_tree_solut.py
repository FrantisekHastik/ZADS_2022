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

def n_min(node):
    index_node = node
    while index_node.left is not None:
        index_node = index_node.left
    return index_node

def n_max(node):
    index_node = node
    while index_node.right is not None:
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

def _t_transplant(tree, replaced_node, moved_node):
    if replaced_node.parent is None:
        _set_root(tree, moved_node)
    else:
        above_node = replaced_node.parent
        if replaced_node == above_node.left:
            _set_left_child(above_node, moved_node)
        else:
            _set_right_child(above_node, moved_node)

def _n_transplant(tree, replaced_node, moved_node):
    _set_left_child(moved_node, replaced_node.left)
    _set_right_child(moved_node, replaced_node.right)
    if tree.root == replaced_node:
        _set_root(tree, moved_node)
    else:
        above_node = replaced_node.parent
        if replaced_node == above_node.left:
            _set_left_child(above_node, moved_node)
        else:
            _set_right_child(above_node, moved_node)

def t_delete(tree, node):
    # Insert code here
    pass

######################################################################

foo = list(range(11))
random.seed(42)
random.shuffle(foo)
test_tree = Tree()
for el in foo:
    t_insert(test_tree, el)

print("Test 1 expects:  (7 (3 (2 (0 - (1 - -)) -) (5 (4 - -) (6 - -))) (8 - (9 - (10 - -))))")
print(f"Test 1 gets:     {to_str(test_tree)}\n")

bar = t_search(test_tree, 5)
print("Test 2 expects:  (5 (4 - -) (6 - -))")
print(f"Test 2 gets:     {to_str(bar)}\n")

bar = t_search(test_tree, 20)
print("Test 3 expects:  -")
print(f"Test 3 gets:     {to_str(bar)}\n")

print("Test 4 expects:  min: (0 - (1 - -))  max: (10 - -)")
print(f"Test 4 gets:     min: {to_str(n_min(test_tree.root))}  max: {to_str(n_max(test_tree.root))}\n")

t_delete(test_tree, t_search(test_tree, 10))
t_delete(test_tree, t_search(test_tree, 0))
t_delete(test_tree, t_search(test_tree, 6))
t_delete(test_tree, t_search(test_tree, 2))
print("Test 5 expects:  (7 (3 (1 - -) (5 (4 - -) -)) (8 - (9 - -)))")
print(f"Test 5 gets:     {to_str(test_tree)}\n")

t_delete(test_tree, t_search(test_tree, 7))
t_delete(test_tree, t_search(test_tree, 3))
print("Test 6 expects:  (8 (4 (1 - -) (5 - -)) (9 - -))")
print(f"Test 6 gets:     {to_str(test_tree)}\n")