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

def _shift_left(node : Node, shift_place : int):
    for i in range(shift_place + 1, MAX_CAPACITY):
        node.keys[i - 1] = node.keys[i]
        node.children[i - 1] = node.children[i]
    node.children[MAX_CAPACITY - 1] = node.children[MAX_CAPACITY]

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
        _set_as_child(new_node, i, node.children[T_PARAMETER + i]) 
    _set_as_child(new_node, MIN_CAPACITY, node.children[MAX_CAPACITY])
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

def _join_nodes(left_part : Node, right_part : Node, mid_value : int):
    result = left_part
    result.keys[result.usage] = mid_value
    result.usage += 1
    for i in range(right_part.usage):
        result.keys[result.usage] = right_part.keys[i]
        _set_as_child(result, result.usage, right_part.children[i])
        result.usage += 1
    _set_as_child(result, result.usage, right_part.children[right_part.usage])
    return result

def b_insert(tree : Tree, key : int):
    if tree.root.usage == MAX_CAPACITY:
        new_root = Node()
        _set_as_child(new_root, 0, tree.root)
        new_root.is_leaf = False
        tree.root = new_root
        _split_child(new_root, 0)
        _insert_nofull(new_root, key)
    else:
        _insert_nofull(tree.root, key)

def b_search(node : Node, key : int):
    index = 0
    while index < node.usage and key > node.keys[index]:
        index += 1
    if index < node.usage and key == node.keys[index]:
        return [node, index]
    elif node.is_leaf:
        return None
    else:
        return b_search(node.children[index], key)

def _b_min(node : Node):
    current_node = node
    while not current_node.is_leaf:
        current_node = current_node.children[0]
    return [current_node, current_node.keys[0]]

def _index_in_parent(node : Node):
    if node.parent is None:
        return None
    else:
        parent_node = node.parent
        for i in range(parent_node.usage + 1):
            if node is parent_node.children[i]:
                return i

def _sibling(node : Node, side : str):
    if node.parent is None:
        return None
    else:
        parent_node = node.parent
        p_index = _index_in_parent(node)
        result = parent_node.children[p_index - 1] if side == "left" else parent_node.children[p_index + 1]
        return result
    
def b_delete(tree : Tree, key : int):
    _n_delete(tree, tree.root, key)

def _n_delete(tree : Tree, node : Node, key : int):
    [target_node, target_index] = b_search(node, key)
    if target_node.is_leaf:
        _shift_left(target_node, target_index)
        target_node.usage -= 1
        rd_node = target_node
    else:
        [rd_node, successor] = _b_min(target_node.children[target_index + 1])
        target_node.keys[target_index] = successor
        _n_delete(tree, rd_node, successor)
    while not (rd_node.parent is None or rd_node.usage >= MIN_CAPACITY):
        parent_index = _index_in_parent(rd_node) 
        if parent_index > 0 and _sibling(rd_node, "left").usage > MIN_CAPACITY:
            sibling_node = _sibling(rd_node, "left")
            _shift_right(rd_node, 0)
            rd_node.keys[0] = rd_node.parent.keys[parent_index - 1]
            rd_node.parent.keys[parent_index - 1] = sibling_node.keys[sibling_node.usage - 1]
            sibling_node.keys[sibling_node.usage - 1] = None
            rd_node.children[0] = sibling_node.children[sibling_node.usage]
            sibling_node.children[sibling_node.usage] = None
            sibling_node.usage -= 1
            rd_node.usage += 1
        elif parent_index < rd_node.parent.usage and _sibling(rd_node, "right").usage > MIN_CAPACITY:
            sibling_node = _sibling(rd_node, "right")
            rd_node.keys[rd_node.usage] = rd_node.parent.keys[parent_index]
            rd_node.parent.keys[parent_index] = sibling_node.keys[0]
            rd_node.children[rd_node.usage + 1] = sibling_node.children[0]
            _shift_left(sibling_node, 0)
            sibling_node.usage -= 1
            rd_node.usage += 1
        else:
            if parent_index > 0:
                sibling_node = _sibling(rd_node, "left")
                new_node = _join_nodes(sibling_node, rd_node, rd_node.parent.keys[parent_index - 1])
                _shift_left(rd_node.parent, parent_index - 1)
                _set_as_child(rd_node.parent, parent_index - 1, new_node)
                rd_node.parent.usage -= 1
                if rd_node.parent is tree.root and rd_node.parent.usage == 0:
                    tree.root = new_node
                    new_node.parent = None
                    return
                rd_node = new_node.parent
            else:
                sibling_node = _sibling(rd_node, "right")
                new_node = _join_nodes(rd_node, sibling_node, rd_node.parent.keys[parent_index])
                _shift_left(rd_node.parent, parent_index)
                _set_as_child(rd_node.parent, parent_index, new_node)
                rd_node.parent.usage -= 1
                if rd_node.parent is tree.root and rd_node.parent.usage == 0:
                    tree.root = new_node
                    new_node.parent = None
                    return
                rd_node = new_node.parent




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

# Test 4: joining left works
b_delete(test_tree_0, 17)
test(test_tree_0, 4, """(k[7, None, None] c['(k[3, None, None] c["(k[0, None, None] c['(k[-1, None, None] c-)', '(k[1, None, None] c-)', None, None])", "(k[5, None, None] c['(k[4, None, None] c-)', '(k[6, None, None] c-)', None, None])", None, None])', '(k[11, None, None] c["(k[9, None, None] c['(k[8, None, None] c-)', '(k[10, None, None] c-)', None, None])", "(k[13, None, None] c['(k[12, None, None] c-)', '(k[15, 16, None] c-)', None, None])", None, None])', None, None])""")

# Test 5: joining right works
b_insert(test_tree_0, -2)
b_insert(test_tree_0, -3)
b_insert(test_tree_0, -4)
b_delete(test_tree_0, -4)
b_delete(test_tree_0, -3)
test(test_tree_0, 5, """(k[7, None, None] c['(k[3, None, None] c["(k[0, None, None] c['(k[-2, -1, None] c-)', '(k[1, None, None] c-)', None, None])", "(k[5, None, None] c['(k[4, None, None] c-)', '(k[6, None, None] c-)', None, None])", None, None])', '(k[11, None, None] c["(k[9, None, None] c['(k[8, None, None] c-)', '(k[10, None, None] c-)', None, None])", "(k[13, None, None] c['(k[12, None, None] c-)', '(k[15, 16, None] c-)', None, None])", None, None])', None, None])""")

# Test 6: chain joining works
b_delete(test_tree_0, 8)
test(test_tree_0, 6, """(k[3, 7, None] c["(k[0, None, None] c['(k[-2, -1, None] c-)', '(k[1, None, None] c-)', None, None])", "(k[5, None, None] c['(k[4, None, None] c-)', '(k[6, None, None] c-)', None, None])", "(k[11, 13, None] c['(k[9, 10, None] c-)', '(k[12, None, None] c-)', '(k[15, 16, None] c-)', None])", None])""")

# Test 6: chain joining and shifting works
b_delete(test_tree_0, 6)
test(test_tree_0, 7, """(k[3, 11, None] c["(k[0, None, None] c['(k[-2, -1, None] c-)', '(k[1, None, None] c-)', None, None])", "(k[7, None, None] c['(k[4, 5, None] c-)', '(k[9, 10, None] c-)', None, None])", "(k[13, None, None] c['(k[12, None, None] c-)', '(k[15, 16, None] c-)', None, None])", None])""")