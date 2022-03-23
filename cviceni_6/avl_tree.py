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
    # insert code here
    pass

def t_search(tree, data):
    index_node = tree.root
    while (index_node is not None) and (index_node.key != data):
        if data < index_node.key:
            index_node = index_node.left
        else:
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
    # insert code here
    pass


######################################################################

# tests will eventually appear