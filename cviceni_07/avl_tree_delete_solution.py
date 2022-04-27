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
    _rebalance_insert(tree, new_node)
    
def _rebalance_insert(tree, node):
    current_node = node.parent
    previous_node = node
    while current_node is not None:
        if previous_node is current_node.left:
            current_node.balance += 1
        else:
            current_node.balance -= 1
        if current_node.balance == 0:
            return
        elif current_node.balance == 1 or current_node.balance == -1:
            previous_node = current_node
            current_node = current_node.parent
        else:  # here begin rotations
            if current_node.balance == 2 and current_node.left.balance == 1:
                new_top = rotate_r(tree, current_node)
                new_top.balance = 0
                new_top.right.balance = 0
                return
            elif current_node.balance == 2 and current_node.left.balance == 0:
                new_top = rotate_r(tree, current_node)
                new_top.balance = -1
                new_top.right.balance = 1
                return
            elif current_node.balance == 2 and current_node.left.balance == -1:
                rotate_l(tree, current_node.left)
                new_top = rotate_r(tree, current_node)
                if new_top.balance == 0:
                    new_top.balance = 0
                    new_top.left.balance = 0
                    new_top.right.balance = 0
                elif new_top.balance == 1:
                    new_top.balance = 0
                    new_top.left.balance = 0
                    new_top.right.balance = -1
                else:
                    new_top.balance = 0
                    new_top.left.balance = 1
                    new_top.right.balance = 0
                return
            elif current_node.balance == -2 and current_node.right.balance == -1:
                new_top = rotate_l(tree, current_node)
                new_top.balance = 0
                new_top.left.balance = 0
                return
            elif current_node.balance == -2 and current_node.right.balance == 0:
                new_top = rotate_l(tree, current_node)
                new_top.balance = 1
                new_top.left.balance = -1
                return
            elif current_node.balance == -2 and current_node.right.balance == 1:
                rotate_r(tree, current_node.right)
                new_top = rotate_l(tree, current_node)
                if new_top.balance == 0:
                    new_top.balance = 0
                    new_top.left.balance = 0
                    new_top.right.balance = 0
                elif new_top.balance == -1:
                    new_top.balance = 0
                    new_top.right.balance = 0
                    new_top.left.balance = 1
                else:
                    new_top.balance = 0
                    new_top.right.balance = -1
                    new_top.left.balance = 0
                return

def t_delete(tree, node):
    if node is None:
        return
    parent_node = node.parent
    side = "left" if (parent_node is None or node is parent_node.left) else "right"
    if node.left is None:
        _t_transplant(tree, node, node.right)
        _rebalance_delete(tree, parent_node, side)
    elif node.right is None:
        _t_transplant(tree, node, node.left)
        _rebalance_delete(tree, parent_node, side)
    else:
        shift_node = n_min(node.right)
        parent_node = shift_node.parent
        side = "right" if (shift_node is node.right) else "left"
        t_delete(tree, shift_node)
        _n_transplant(tree, node, shift_node)
        _rebalance_delete(tree, parent_node, side)

def _rebalance_delete(tree, node, side):
    current_node = node
    going_from = side
    while current_node is not None:
        if going_from == "left":
            current_node.balance -= 1
        else:
            current_node.balance += 1
        if abs(current_node.balance) == 1:
            return
        elif current_node.balance == 0:
            going_from = "left" if (current_node.parent is None or current_node is current_node.parent.left) else "right"
            current_node = current_node.parent
        else:  # here begin rotations
            parent_node = current_node.parent
            going_from = "left" if (parent_node is None or current_node is parent_node.left) else "right"
            if current_node.balance == 2 and current_node.left.balance == 1:
                new_top = rotate_r(tree, current_node)
                new_top.balance = 0
                new_top.right.balance = 0
                current_node = parent_node
            elif current_node.balance == 2 and current_node.left.balance == 0:
                new_top = rotate_r(tree, current_node)
                new_top.balance = -1
                new_top.right.balance = 1
                return
            elif current_node.balance == 2 and current_node.left.balance == -1:
                rotate_l(tree, current_node.left)
                new_top = rotate_r(tree, current_node)
                if new_top.balance == 0:
                    new_top.balance = 0
                    new_top.left.balance = 0
                    new_top.right.balance = 0
                elif new_top.balance == 1:
                    new_top.balance = 0
                    new_top.left.balance = 0
                    new_top.right.balance = -1
                else:
                    new_top.balance = 0
                    new_top.left.balance = 1
                    new_top.right.balance = 0
                current_node = parent_node
            elif current_node.balance == -2 and current_node.right.balance == -1:
                new_top = rotate_l(tree, current_node)
                new_top.balance = 0
                new_top.left.balance = 0
                current_node = parent_node
            elif current_node.balance == -2 and current_node.right.balance == 0:
                new_top = rotate_l(tree, current_node)
                new_top.balance = 1
                new_top.left.balance = -1
                return
            elif current_node.balance == -2 and current_node.right.balance == 1:
                rotate_r(tree, current_node.right)
                new_top = rotate_l(tree, current_node)
                if new_top.balance == 0:
                    new_top.balance = 0
                    new_top.left.balance = 0
                    new_top.right.balance = 0
                elif new_top.balance == -1:
                    new_top.balance = 0
                    new_top.right.balance = 0
                    new_top.left.balance = 1
                else:
                    new_top.balance = 0
                    new_top.right.balance = -1
                    new_top.left.balance = 0
                current_node = parent_node


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
