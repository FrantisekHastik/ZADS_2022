from cgi import test


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
    index = node.next
    while index is not None:
        result = result + ", " +  str(index.key)
        index = index.next
    result = result + "]"
    return result

def len(list):
    return list.length

def insert_start(list, el):
    new_node = Node(el)
    new_node.next = list.sentinel.next
    list.sentinel.next = new_node
    list.sentinel.next.prev = new_node
    new_node.previous = list.sentinel

def nth(list, n):
    # Insert code here
    pass

def insert_nth(list, n, el):
    # Insert code here
    pass

def delete_nth(list, n):
    # Insert code here
    pass

def concatenate(list_1, list_2):
    # Insert code here
    pass


foo = [i for i in range(2, 50) if 0 not in [i % n for n in range(2, i)]]
test_list = List()
for el in foo:
    insert_start(test_list, el)
print("Test 1 expects:  [47, 43, 41, 37, 31, 29, 23, 19, 17, 13, 11, 7, 5, 3, 2]")
print(f"Test 1 gets:     {to_str(test_list)}\n")

for n in range(5):
    delete_nth(test_list, n)
delete_nth(test_list, 7)
print("Test 2 expects:  [47, 23, 19, 17, 13, 11, 7, 5, 2]")
print(f"Test 2 gets:     {to_str(test_list)}\n")

for bar in range(3):
    insert_start(test_list, bar)
test_list = insert_nth(test_list, 10, 100)
print("Test 3 expects:  [47, 2, 1, 0, 23, 19, 17, 13, 11, 7, 100, 5, 2]")
print(f"Test 3 gets:     {to_str(test_list)}\n")

baz = [101, 102, 103]
test_list_2 = List()
for el in foo:
    insert_start(test_list_2, el)


print("Test 4 expects:  [47, 2, 1, 0, 23, 19, 17, 13, 11, 7, 100, 5, 2, 101, 102, 103]")
print(f"Test 4 gets:     {to_str(concatenate(test_list, test_list_2))}\n")