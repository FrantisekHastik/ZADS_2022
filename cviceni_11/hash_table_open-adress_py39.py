import hashlib
import string 
import random

def to_str(obj):
    if isinstance(obj, HashTableOA):
        result = to_str(obj.data)
    elif isinstance(obj, list):
        result = str(list(map(to_str, obj)))
    elif obj is None:
        result = None
    else:
        result = str(obj)
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

def gen_string(size):
    charset = string.ascii_letters + string.digits
    return ''.join(random.choice(charset) for _ in range(size))

######################################################################

class HashTableOA:
    def __init__(self, size):
        self.size = size
        self.data = [None] * size
        self.sequence = lambda key, index: (self._hash(key) + index) % self.size

    def _hash(self, key):
        return int(hashlib.sha1(key.encode("utf-8")).hexdigest(), 16) % 10**6

    def set_sequence(self, type):
        if type == "LINEAR":
            self.sequence = lambda key, index: (self._hash(key) + index) % self.size
        elif type == "QUADRATIC":
            self.sequence = lambda key, index: (self._hash(key) + 7 * index + 13 * (index ** 2)) % self.size
        elif type == "DOUBLE":
            self.sequence = lambda key, index: (self._hash(key) + index * (1 + (self._hash(key) % (self.size) - 1))) % self.size
        else:
            return

######################################################################

def htoa_insert(table: HashTableOA, key):
    # insert code here
    pass

def htoa_search(table: HashTableOA, key):
    # insert code here
    return

def htoa_delete(table: HashTableOA, key):
    # insert code here
    pass

######################################################################

test_ht = HashTableOA(30)
test(test_ht, "[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]")

random.seed(42)
for _ in range(20):
    htoa_insert(test_ht, gen_string(4))
test(test_ht, "[None, None, None, 'OhbV', '5IfL', 'Bcbf', 'xKmT', 'rpoi', 'noGM', '2wMq', 'ZcUD', None, 'Z3aW', 'vrjn', 'fygw', 'Ih7y', 'ZkSB', 'ON43', None, None, 'VgRV', None, None, 'PSIA', 'bJmT', 'oCLr', None, 'fJs1', None, '9Wvg']")

for i in ['ZcUD', 'vrjn', '9Wvg', 'Z3aW', 'fygw']:
    htoa_delete(test_ht, i)
test(test_ht, "[None, None, None, 'OhbV', '5IfL', 'Bcbf', 'xKmT', 'rpoi', 'noGM', '2wMq', 'FREE', None, 'FREE', 'FREE', 'FREE', 'Ih7y', 'ZkSB', 'ON43', None, None, 'VgRV', None, None, 'PSIA', 'bJmT', 'oCLr', None, 'fJs1', None, 'FREE']")


test_ht = HashTableOA(30)
test_ht.set_sequence("QUADRATIC")
random.seed(42)
for _ in range(20):
    htoa_insert(test_ht, gen_string(4))
test(test_ht, "[None, None, 'vrjn', 'OhbV', '5IfL', 'Bcbf', 'xKmT', 'rpoi', None, None, None, 'ON43', 'Z3aW', '2wMq', None, 'ZcUD', 'ZkSB', 'fJs1', 'fygw', None, 'VgRV', 'Ih7y', None, 'PSIA', 'bJmT', 'oCLr', None, 'noGM', None, '9Wvg']")

for i in ['ZcUD', 'vrjn', '9Wvg', 'Z3aW', 'fygw']:
    htoa_delete(test_ht, i)
test(test_ht, "[None, None, 'FREE', 'OhbV', '5IfL', 'Bcbf', 'xKmT', 'rpoi', None, None, None, 'ON43', 'FREE', '2wMq', None, 'FREE', 'ZkSB', 'fJs1', 'FREE', None, 'VgRV', 'Ih7y', None, 'PSIA', 'bJmT', 'oCLr', None, 'noGM', None, 'FREE']")


test_ht = HashTableOA(30)
test_ht.set_sequence("DOUBLE")
random.seed(42)
for _ in range(20):
    htoa_insert(test_ht, gen_string(4))
test(test_ht, "['ON43', None, None, 'OhbV', '5IfL', 'Bcbf', 'vrjn', 'rpoi', None, None, None, None, 'Z3aW', None, 'noGM', 'Ih7y', 'ZkSB', None, 'fygw', None, 'VgRV', '2wMq', None, 'PSIA', 'bJmT', 'oCLr', None, 'fJs1', 'ZcUD', '9Wvg']")

for i in ['ZcUD', 'vrjn', '9Wvg', 'Z3aW', 'fygw']:
    htoa_delete(test_ht, i)
test(test_ht, "['ON43', None, None, 'OhbV', '5IfL', 'Bcbf', 'FREE', 'rpoi', None, None, None, None, 'FREE', None, 'noGM', 'Ih7y', 'ZkSB', None, 'FREE', None, 'VgRV', '2wMq', None, 'PSIA', 'bJmT', 'oCLr', None, 'fJs1', 'FREE', 'FREE']")

