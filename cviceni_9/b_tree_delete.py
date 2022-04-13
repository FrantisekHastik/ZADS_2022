T_PARAMETER = 2
MAX_CAPACITY = 2 * T_PARAMETER - 1
MIN_CAPACITY = T_PARAMETER - 1

class Node:
    def __init__(self):
        self.keys = [None] * MAX_CAPACITY
        self.children = [None] * (MAX_CAPACITY + 1)
        self.parent = None
        self.usage = 0
        self.is_leaf = True

class Tree:
    def __init__(self):
        self.root = Node()

def to_str(obj):
    if isinstance(obj, Tree):
        result = to_str(obj.root)
    elif isinstance(obj, Node):
        result = f"(k{obj.keys} c{to_str(obj.children)})"
        result = result.translate({ord(i): None for i in '\\'})
    elif isinstance(obj, list):
        temp = list(map(to_str, obj))
        result = "-" if temp.count(None) == len(temp) else str(temp)
    elif isinstance(obj, int):
        result = str(obj)
    elif obj is None:
        result = None
    return result

def test(tree, num, expectation):
    p = "passed."
    f = "failed."
    result = to_str(tree)
    print(f"Test {num} expects:  {expectation}")
    print(f"Test {num} gets:     {result}")
    print(f"Test {num} {p if expectation == result else f}\n")

######################################################################

def _shift_right(node : Node, shift_place : int):
    node.children[node.usage + 1] = node.children[node.usage]
    for i in range(node.usage, shift_place, -1):
        node.keys[i] = node.keys[i - 1]
        node.children[i] = node.children[i - 1]

def _shift_keys_left(node : Node, shift_place : int):
    node.children[node.usage + 1] = node.children[node.usage]
    for i in range(shift_place + 1, MAX_CAPACITY):
        node.keys[i - 1] = node.keys[i]

def _b_min(node):
    current_node = node
    while not current_node.is_leaf:
        current_node = current_node.children[0]
    return [current_node, current_node.keys[0]]

def _set_as_child(parent_node : Node, index : int, child_node : Node):
    parent_node.children[index] = child_node
    if child_node is not None:
        child_node.parent = parent_node

def _split_node(node : Node):
    med_value = node.keys[MIN_CAPACITY]

    new_node = Node()
    new_node.is_leaf = node.is_leaf
    new_node.parent = node.parent
    new_node.usage = MIN_CAPACITY

    for i in range(MIN_CAPACITY):
        new_node.keys[i] = node.keys[T_PARAMETER + i]
        new_node.children[i] = node.children[T_PARAMETER + i]
    new_node.children[MIN_CAPACITY] = node.children[MAX_CAPACITY]
    for j in range(MIN_CAPACITY, MAX_CAPACITY):
        node.keys[j] = None
        node.children[j + 1] = None

    node.usage = MIN_CAPACITY
    return med_value, node, new_node

def _split_child(parent_node : Node, child_index : int):
    [med_value, left_part, right_part] = _split_node(parent_node.children[child_index])
    _shift_right(parent_node, child_index)
    _set_as_child(parent_node, child_index, left_part)
    _set_as_child(parent_node, child_index + 1, right_part)
    parent_node.keys[child_index] = med_value
    parent_node.usage += 1

######################################################################

def _insert_nofull(node : Node, key : int):
    index = 0
    while index < node.usage and key > node.keys[index]:
        index += 1
    
    if node.is_leaf:
        _shift_right(node, index)
        node.keys[index] = key
        node.usage += 1
    else:
        if node.children[index].usage == MAX_CAPACITY:
            _split_child(node, index)
            if key > node.keys[index]:
                index += 1
        _insert_nofull(node.children[index], key)

def b_insert(tree : Tree, key : int):
    if tree.root.usage == MAX_CAPACITY:
        new_root = Node()
        new_root.children[0] = tree.root
        new_root.is_leaf = False
        tree.root = new_root
        _split_child(new_root, 0)
        _insert_nofull(new_root, key)
    else:
        _insert_nofull(tree.root, key)

def b_search(node : Node, key : int):
    # insert your code here
    return [node, key]

def b_delete(tree : Tree, key : int):
    _n_delete(tree.root, key)

def _n_delete(node : Node, key : int):
    # insert your code here
    pass


######################################################################

# Test 0: structure works
test_tree_0 = Tree()
test(test_tree_0, 0, "(k[None, None, None] c-)")

# Test 1: insert works
for i in range(18):
    b_insert(test_tree_0, i)
b_insert(test_tree_0, -1)
test(test_tree_0, 1, """(k[7, None, None] c['(k[3, None, None] c["(k[1, None, None] c['(k[-1, 0, None] c-)', '(k[2, None, None] c-)', None, None])", "(k[5, None, None] c['(k[4, None, None] c-)', '(k[6, None, None] c-)', None, None])", None, None])', '(k[11, None, None] c["(k[9, None, None] c['(k[8, None, None] c-)', '(k[10, None, None] c-)', None, None])", "(k[13, 15, None] c['(k[12, None, None] c-)', '(k[14, None, None] c-)', '(k[16, 17, None] c-)', None])", None, None])', None, None])""")

# Test 2: search works
test(b_search(test_tree_0.root, 15), 2, """["(k[13, 15, None] c['(k[12, None, None] c-)', '(k[14, None, None] c-)', '(k[16, 17, None] c-)', None])", '1']""")

# Test 3: shifting works
b_delete(test_tree_0, 2)
b_delete(test_tree_0, 14)
test(test_tree_0, 3, """(k[7, None, None] c['(k[3, None, None] c["(k[0, None, None] c['(k[-1, None, None] c-)', '(k[1, None, None] c-)', None, None])", "(k[5, None, None] c['(k[4, None, None] c-)', '(k[6, None, None] c-)', None, None])", None, None])', '(k[11, None, None] c["(k[9, None, None] c['(k[8, None, None] c-)', '(k[10, None, None] c-)', None, None])", "(k[13, 16, None] c['(k[12, None, None] c-)', '(k[15, None, None] c-)', '(k[17, None, None] c-)', None])", None, None])', None, None])""")