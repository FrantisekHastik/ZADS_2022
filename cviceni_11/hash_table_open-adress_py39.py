import os
import sys
import string 
import random
hashseed = os.getenv('PYTHONHASHSEED')
if not hashseed:
    os.environ['PYTHONHASHSEED'] = '0'
    os.execv(sys.executable, [sys.executable] + sys.argv)

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
        return hash(key) % self.size

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
test(test_ht, "[None, None, None, 'OhbV', 'Z3aW', 'bJmT', '5IfL', 'vrjn', 'noGM', 'VgRV', 'rpoi', '2wMq', None, None, None, 'PSIA', None, None, 'Bcbf', 'oCLr', '9Wvg', 'ON43', 'ZcUD', 'xKmT', 'fJs1', None, 'Ih7y', 'ZkSB', 'fygw', None]")

for i in ['ZcUD', 'vrjn', '9Wvg', 'Z3aW', 'fygw']:
    htoa_delete(test_ht, i)
test(test_ht, "[None, None, None, 'OhbV', 'FREE', 'bJmT', '5IfL', 'FREE', 'noGM', 'VgRV', 'rpoi', '2wMq', None, None, None, 'PSIA', None, None, 'Bcbf', 'oCLr', 'FREE', 'ON43', 'FREE', 'xKmT', 'fJs1', None, 'Ih7y', 'ZkSB', 'FREE', None]")


test_ht = HashTableOA(30)
test_ht.set_sequence("QUADRATIC")
random.seed(42)
for _ in range(20):
    htoa_insert(test_ht, gen_string(4))
test(test_ht, "[None, None, None, 'OhbV', 'vrjn', 'bJmT', '5IfL', None, 'noGM', 'VgRV', 'rpoi', None, None, None, 'fJs1', 'PSIA', None, 'fygw', 'Bcbf', '9Wvg', 'xKmT', 'ON43', 'ZcUD', 'Z3aW', 'oCLr', None, 'Ih7y', 'ZkSB', '2wMq', None]")

for i in ['ZcUD', 'vrjn', '9Wvg', 'Z3aW', 'fygw']:
    htoa_delete(test_ht, i)
test(test_ht, "[None, None, None, 'OhbV', 'FREE', 'bJmT', '5IfL', None, 'noGM', 'VgRV', 'rpoi', None, None, None, 'fJs1', 'PSIA', None, 'FREE', 'Bcbf', 'FREE', 'xKmT', 'ON43', 'FREE', 'FREE', 'oCLr', None, 'Ih7y', 'ZkSB', '2wMq', None]")


test_ht = HashTableOA(30)
test_ht.set_sequence("DOUBLE")
random.seed(42)
for _ in range(20):
    htoa_insert(test_ht, gen_string(4))
test(test_ht, "['fJs1', None, None, 'OhbV', 'vrjn', 'bJmT', '5IfL', None, 'noGM', 'VgRV', 'rpoi', None, 'Z3aW', None, None, 'PSIA', '2wMq', None, 'Bcbf', '9Wvg', 'xKmT', 'fygw', 'ZcUD', None, 'oCLr', None, 'Ih7y', 'ZkSB', None, None]")

for i in ['ZcUD', 'vrjn', '9Wvg', 'Z3aW', 'fygw']:
    htoa_delete(test_ht, i)
test(test_ht, "['fJs1', None, None, 'OhbV', 'FREE', 'bJmT', '5IfL', None, 'noGM', 'VgRV', 'rpoi', None, 'FREE', None, None, 'PSIA', '2wMq', None, 'Bcbf', 'FREE', 'xKmT', 'FREE', 'FREE', None, 'oCLr', None, 'Ih7y', 'ZkSB', None, None]")