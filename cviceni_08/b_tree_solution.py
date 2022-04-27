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
    elif isinstance(obj, list):
        temp = list(map(to_str, obj))
        result = "-" if temp.count(None) == len(temp) else temp
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
        

######################################################################

# Test 0: structure works
test_tree_0 = Tree()
test(test_tree_0, 0, "(k[None, None, None] c-)")

# Test 1: basic insert into root works
b_insert(test_tree_0, 50)
b_insert(test_tree_0, 70)
b_insert(test_tree_0, 80)
test(test_tree_0, 1, "(k[50, 70, 80] c-)")

# Test 2: splitting root works
b_insert(test_tree_0, 90)
b_insert(test_tree_0, 60)
test(test_tree_0, 2, "(k[70, None, None] c['(k[50, 60, None] c-)', '(k[80, 90, None] c-)', None, None])")

# Test 3: splitting in leaf works
b_insert(test_tree_0, 73)
b_insert(test_tree_0, 76)
b_insert(test_tree_0, 61)
test(test_tree_0, 3, "(k[70, 80, None] c['(k[50, 60, 61] c-)', '(k[73, 76, None] c-)', '(k[90, None, None] c-)', None])")

# Test 4: splitting in leaf works again
b_insert(test_tree_0, 62)
test(test_tree_0, 4, "(k[60, 70, 80] c['(k[50, None, None] c-)', '(k[61, 62, None] c-)', '(k[73, 76, None] c-)', '(k[90, None, None] c-)'])")

# Test 5: cascading or preemptive splitting works
b_insert(test_tree_0, 51)
b_insert(test_tree_0, 52)
b_insert(test_tree_0, 53)
test(test_tree_0, 5, """(k[70, None, None] c["(k[51, 60, None] c['(k[50, None, None] c-)', '(k[52, 53, None] c-)', '(k[61, 62, None] c-)', None])", "(k[80, None, None] c['(k[73, 76, None] c-)', '(k[90, None, None] c-)', None, None])", None, None])""")