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