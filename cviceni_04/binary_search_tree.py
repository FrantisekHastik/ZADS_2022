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
    # Insert code here
    pass

def t_search(tree, data):
    # Insert code here
    return None

def n_min(node):
    # Insert code here
    return None

def n_max(node):
    # Insert code here
    return None

def _set_left_child(parent_node, new_child_node):
    # Insert code here
    pass

def _set_right_child(parent_node, new_child_node):
    # Insert code here
    pass

def _set_root(tree, new_root):
    # Insert code here
    pass

def _t_transplant(tree, replaced_node, moved_node):
    # Insert code here
    pass

def n_transplant(tree, replaced_node, moved_node):
    # Insert code here
    pass

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