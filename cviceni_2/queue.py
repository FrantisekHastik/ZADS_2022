class Queue:
    def __init__(self, size):
        self.data = [None] * size
        self.head = 0
        self.tail = 0

def q_enque(stack, value):
    return 42

def q_deque(stack):
    return 42

s = Queue(20)
q_enque(s, 2)
q_enque(s, 4)
q_enque(s, 8)
print("Test 1 expects: 2")
print("Test 1 gets:    " + str(q_deque(s)))
print("Test 2 expects: 4")
print("Test 2 gets:    " + str(q_deque(s)))
print("Test 3 expects: 8")
print("Test 3 gets:    " + str(q_deque(s)))
print("Test 4 expects: Error message")
print("Test 4 gets:    " + str(q_deque(s)))