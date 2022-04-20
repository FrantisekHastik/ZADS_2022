class Node:
    def __init__(self, key):
        self.key = key
        self.next = None
        self.previous = None

class List:
    def __init__(self):
        self.sentinel = Node(None)
        self.length = 0

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

def l_search(list, key):
    index_node = list.sentinel.next
    index = 0
    while index_node is not None:
        if key == index_node.key:
            return index, index_node
        else:
            index_node = index_node.next
            index += 1
    return None

######################################################################

class HashTableChain:
    def __init__(self, size):
        self.size = size
        self.data = [None] * size
        for i in range(size):
            self.data[i] = List()

def to_str(obj):
    if isinstance(obj, HashTableChain):
        result = to_str(obj.data)
    elif isinstance(obj, List):
        node = obj.sentinel.next
        result = ("[" + str(node.key)) if node is not None else "["
        index_node = node.next if node is not None else node
        while index_node is not None:
            result = result + ", " + str(index_node.key)
            index_node = index_node.next
        result = result + "]"
    elif isinstance(obj, list):
        result = str(list(map(to_str, obj)))
    elif isinstance(obj, int):
        result = str(obj)
    elif obj is None:
        result = None
    return result
    
TEST_NUMBER = 0    
def test(obj, expectation):
    global TEST_NUMBER
    p = "passed."
    f = "failed."
    result = to_str(obj)
    print(f"Test {TEST_NUMBER} expects:  {expectation}")
    print(f"Test {TEST_NUMBER} gets:     {result}")
    print(f"Test {TEST_NUMBER} {p if expectation == result else f}\n")
    TEST_NUMBER += 1

######################################################################

def htc_hash(table : HashTableChain, key : int):
    limit = table.size
    temp = ((key + 13) * 15319) ** 2
    return temp % limit

def htc_insert(table: HashTableChain, key : int):
    # insert code here
    pass

def htc_search(table: HashTableChain, key : int):
    # insert code here
    return

def htc_delete(table: HashTableChain, key : int):
    # insert code here
    pass

######################################################################

# Test 0: to_str works
test_ht = HashTableChain(11)
test(test_ht, "['[]', '[]', '[]', '[]', '[]', '[]', '[]', '[]', '[]', '[]', '[]']")

# Test 1: insert works
for i in range(20):
    htc_insert(test_ht, i)
test(test_ht, "['[9]', '[17, 12, 6, 1]', '[]', '[16, 13, 5, 2]', '[15, 14, 4, 3]', '[19, 10, 8]', '[]', '[]', '[]', '[18, 11, 7, 0]', '[]']")

# Test 2: search and delete works
for i in range(5):
    htc_delete(test_ht, i)
test(test_ht, "['[9]', '[17, 12, 6]', '[]', '[16, 13, 5]', '[15, 14]', '[19, 10, 8]', '[]', '[]', '[]', '[18, 11, 7]', '[]']")
