class Node:
    def __init__(self, key):
        self.key = key
        self.next = None

def to_str(node):
    result = "[" + str(node.key)
    index = node.next
    while index is not None:
        result = result + ", " +  str(index.key)
        index = index.next
    result = result + "]"
    return result

def length(node):
    result = 0
    index = node
    while index != None:
        index = index.next
        result += 1
    return result

def insert_after(node, el):
    new_node = Node(el)
    new_node.next = node.next
    node.next = new_node

def delete_after(node):
    result = node.next
    if result is not None:
       node.next = node.next.next
    return result

def nth(node, n):
    index = 0
    result_node = node
    while result_node != None and index < n:
        result_node = result_node.next
        index += 1
    return result_node

def find(node, key):
    index = node
    while index is not None and index.key != key:
        index = index.next
    return index

def member(node, key):
    return find(node, key) is not None

def insert_nth(node, n, el):
    if n == 0:
        new_node = Node(el)
        new_node.next = node
        return new_node
    else:
        before_node = nth(node, n - 1)
        insert_after(before_node, el)
        return node
    
    

    
    


foo = [i for i in range(2, 46) if 0 not in [i % n for n in range(2, i)]]
test_list = Node(47)
for el in foo:
    insert_after(test_list, el)
print("Test 1 expects:  [47, 43, 41, 37, 31, 29, 23, 19, 17, 13, 11, 7, 5, 3, 2]")
print(f"Test 1 gets:     {to_str(test_list)}\n")

for _ in range(5):
    delete_after(test_list)
delete_after(nth(test_list, 7))
print("Test 2 expects:  [47, 23, 19, 17, 13, 11, 7, 5, 2]")
print(f"Test 2 gets:     {to_str(test_list)}\n")

for bar in range(3):
    insert_after(test_list, bar)
test_list = insert_nth(test_list, 10, 100)
print("Test 3 expects:  [47, 2, 1, 0, 23, 19, 17, 13, 11, 7, 100, 5, 2]")
print(f"Test 3 gets:     {to_str(test_list)}\n")