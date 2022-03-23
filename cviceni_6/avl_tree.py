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
    # insert code here
    return

def rotate_l(tree, node):
    # insert code here
    return
    
def t_insert(tree, element):
    # insert code here
    pass

def _rebalance(tree, node):
    # insert code here
    pass


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