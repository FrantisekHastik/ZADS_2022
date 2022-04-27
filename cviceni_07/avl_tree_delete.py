import random

class Node:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None
        self.balance = 0

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

def test(tree, num, expectation):
    p = "passed."
    f = "failed."
    result = to_str(tree)
    print(f"Test {num} expects:  {expectation}")
    print(f"Test {num} gets:     {result}")
    print(f"Test {num} {p if expectation == result else f}\n")

######################################################################

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
    moved_node.balance = replaced_node.balance
    if tree.root == replaced_node:
        _set_root(tree, moved_node)
    else:
        above_node = replaced_node.parent
        if replaced_node == above_node.left:
            _set_left_child(above_node, moved_node)
        else:
            _set_right_child(above_node, moved_node)

############################################################

def rotate_r(tree, node):
    ascending_node = node.left
    moved_subtree = ascending_node.right
    parent_node = node.parent
    if parent_node is not None:
        if node is parent_node.left:
            _set_left_child(parent_node, ascending_node)
        else:
            _set_right_child(parent_node, ascending_node)
    else:
        _set_root(tree, ascending_node)
    _set_left_child(node, moved_subtree)
    _set_right_child(ascending_node, node)
    return ascending_node

def rotate_l(tree, node):
    ascending_node = node.right
    moved_subtree = ascending_node.left
    parent_node = node.parent
    if parent_node is not None:
        if node is parent_node.left:
            _set_left_child(parent_node, ascending_node)
        else:
            _set_right_child(parent_node, ascending_node)
    else:
        _set_root(tree, ascending_node)
    _set_right_child(node, moved_subtree)
    _set_left_child(ascending_node, node)
    return ascending_node

def t_search(tree, data):
    index_node = tree.root
    while (index_node is not None) and (index_node.key != data):
        if data < index_node.key:
            index_node = index_node.left
        else:
            index_node = index_node.right
    return index_node

######################################################################

def t_insert(tree, element):
    # Insert code here
    pass
    
def _rebalance_insert(tree, node):
    # Insert code here
    pass

def t_delete(tree, node):
    # Insert code here
    pass

def _rebalance_delete(tree, node, side):
    # Insert code here
    pass


######################################################################

# Test 0: tests correct insert
foo = list(range(15))
test_tree_0 = Tree()
test_tree_1 = Tree()
for el in foo:
    t_insert(test_tree_0, el)
    t_insert(test_tree_1, el)
test(test_tree_0, 0, "(7 (3 (1 (0 - -) (2 - -)) (5 (4 - -) (6 - -))) (11 (9 (8 - -) (10 - -)) (13 (12 - -) (14 - -))))")

# Test 1: tests (-2 0) rotation
t_delete(test_tree_0, t_search(test_tree_0, 0))
t_delete(test_tree_0, t_search(test_tree_0, 1))
t_delete(test_tree_0, t_search(test_tree_0, 2))  # rotation should occur here
test(test_tree_0, 1, "(7 (5 (3 - (4 - -)) (6 - -)) (11 (9 (8 - -) (10 - -)) (13 (12 - -) (14 - -))))")

# Test 2: tests (0 2) rotation
t_delete(test_tree_1, t_search(test_tree_1, 14))
t_delete(test_tree_1, t_search(test_tree_1, 13))
t_delete(test_tree_1, t_search(test_tree_1, 12))  # rotation should occur here
test(test_tree_1, 2, "(7 (3 (1 (0 - -) (2 - -)) (5 (4 - -) (6 - -))) (9 (8 - -) (11 (10 - -) -)))")

# Test 3: tests removing node with two children and (-2 -1) rotation
t_delete(test_tree_1, t_search(test_tree_1, 10))
t_insert(test_tree_1, 12)
t_delete(test_tree_1, t_search(test_tree_1, 7)) # rotation should occur here
test(test_tree_1, 3, "(8 (3 (1 (0 - -) (2 - -)) (5 (4 - -) (6 - -))) (11 (9 - -) (12 - -)))")

# Test 4: tests removing node with two children and (1 2) rotation
t_delete(test_tree_1, t_search(test_tree_1, 6))
t_delete(test_tree_1, t_search(test_tree_1, 5))
t_delete(test_tree_1, t_search(test_tree_1, 4))
test(test_tree_1, 4, "(8 (1 (0 - -) (3 (2 - -) -)) (11 (9 - -) (12 - -)))")


# Test 5: tests (-1 2) rotation, (-2 1) rotation and chain rotations
t_insert(test_tree_0, 15)
t_delete(test_tree_0, t_search(test_tree_0, 6))  # (-1 2) and (-2 1) rotations should occur
test(test_tree_0, 5, "(11 (7 (4 (3 - -) (5 - -)) (9 (8 - -) (10 - -))) (13 (12 - -) (14 - (15 - -))))")
