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
    _rebalance(tree, new_node)

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
    
def _rebalance(tree, node):
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


######################################################################

foo = list(range(7))
test_tree_0 = Tree()
for el in foo:
    t_insert(test_tree_0, el)

print("Test 1 expects:  (3 (1 (0 - -) (2 - -)) (5 (4 - -) (6 - -)))")
print(f"Test 1 gets:     {to_str(test_tree_0)}\n")

bar = list(range(7))
bar.reverse()
test_tree_1 = Tree()
for el in bar:
    t_insert(test_tree_1, el)

print("Test 2 expects:  (3 (1 (0 - -) (2 - -)) (5 (4 - -) (6 - -)))")
print(f"Test 2 gets:     {to_str(test_tree_1)}\n")

baz = [4, 5, 1, 0, 2, 3, 6]
test_tree_2 = Tree()
for el in baz:
    t_insert(test_tree_2, el)

print("Test 3 expects:  (2 (1 (0 - -) -) (4 (3 - -) (5 - (6 - -))))")
print(f"Test 3 gets:     {to_str(test_tree_2)}\n")

why = [2, 1, 5, 6, 4, 3, 0]
test_tree_2 = Tree()
for el in why:
    t_insert(test_tree_2, el)

print("Test 4 expects:  (4 (2 (1 (0 - -) -) (3 - -)) (5 - (6 - -)))")
print(f"Test 4 gets:     {to_str(test_tree_2)}\n")

ran = list(range(63))
random.seed(42)
random.shuffle(ran)
test_tree_3 = Tree()
for el in ran:
    t_insert(test_tree_3, el)
ran_res = to_str(test_tree_3)
ran_exp = "(36 (21 (11 (6 (3 (1 (0 - -) (2 - -)) (5 (4 - -) -)) (9 (8 (7 - -) -) (10 - -))) (18 (15 (13 (12 - -) (14 - -)) (16 - (17 - -))) (19 - (20 - -)))) (29 (25 (23 (22 - -) (24 - -)) (27 (26 - -) (28 - -))) (33 (31 (30 - -) (32 - -)) (35 (34 - -) -)))) (48 (41 (38 (37 - -) (39 - (40 - -))) (44 (42 - (43 - -)) (46 (45 - -) (47 - -)))) (53 (51 (50 (49 - -) -) (52 - -)) (57 (55 (54 - -) (56 - -)) (61 (59 (58 - -) (60 - -)) (62 - -))))))"
p = "passed."
f = "failed."

print(f"Test 5 expects:  {ran_exp}")
print(f"Test 5 gets:     {ran_res}")
print(f"Test 5 {p if ran_res == ran_exp else f}\n")
