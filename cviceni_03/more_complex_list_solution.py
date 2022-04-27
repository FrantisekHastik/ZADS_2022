class Node:
    def __init__(self, key):
        self.key = key
        self.next = None
        self.previous = None

class List:
    def __init__(self):
        self.sentinel = Node(None)
        self.length = 0

def to_str(list):
    node = list.sentinel.next
    result = "[" + str(node.key)
    index_node = node.next
    while index_node is not None:
        result = result + ", " + str(index_node.key)
        index_node = index_node.next
    result = result + "]"
    return result

def length(list):
    return list.length

def insert_start(list, el):
    new_node = Node(el)

    new_node.next = list.sentinel.next
    new_node.previous = list.sentinel
    if list.sentinel.next is not None:
        list.sentinel.next.previous = new_node
    list.sentinel.next = new_node
    list.length += 1
    

def nth(list, n):
    index = -1
    result_node = list.sentinel
    while result_node != None and index < n:
        result_node = result_node.next
        index += 1
    return result_node

def insert_nth(list, n, el):
    previous_node = nth(list, n - 1)
    new_node = Node(el)

    new_node.next = previous_node.next
    new_node.previous = previous_node
    previous_node.next.previous = new_node
    previous_node.next = new_node
    list.length += 1


def delete_nth(list, n):
    if n >= 0:    
        deleted_node = nth(list, n)
        previous_node = deleted_node.previous
        next_node = deleted_node.next
        
        previous_node.next = next_node
        if next_node is not None:
            next_node.previous = previous_node
        list.length -= 1
        return deleted_node.key
    else:
        return None
    

def concatenate(list_1, list_2):
    connect_node = nth(list_1, length(list_1) - 1)
    connect_node.next = list_2.sentinel.next
    connect_node.next.previous = connect_node
    list_1.length += list_2.length
    return list_1



foo = [i for i in range(2, 50) if 0 not in [i % n for n in range(2, i)]]
test_list = List()
for el in foo:
    insert_start(test_list, el)
print("Test 1 expects:  [47, 43, 41, 37, 31, 29, 23, 19, 17, 13, 11, 7, 5, 3, 2]")
print(f"Test 1 gets:     {to_str(test_list)}\n")

for n in range(5):
    delete_nth(test_list, n)
delete_nth(test_list, 7)
print("Test 2 expects:  [43, 37, 29, 19, 13, 11, 7, 3, 2]")
print(f"Test 2 gets:     {to_str(test_list)}\n")

for bar in range(3):
    insert_start(test_list, bar)
insert_nth(test_list, 10, 100)
print("Test 3 expects:  [2, 1, 0, 43, 37, 29, 19, 13, 11, 7, 100, 3, 2]")
print(f"Test 3 gets:     {to_str(test_list)}\n")

baz = [101, 102, 103]
test_list_2 = List()
for el in baz:
    insert_start(test_list_2, el)
print("Test 4 expects:  [2, 1, 0, 43, 37, 29, 19, 13, 11, 7, 100, 3, 2, 103, 102, 101]")
print(f"Test 4 gets:     {to_str(concatenate(test_list, test_list_2))}\n")
print("Test 5 expects:  16")
print(f"Test 5 gets:     {length(test_list)}\n")