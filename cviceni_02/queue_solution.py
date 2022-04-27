class Queue:
    def __init__(self, size):
        self.data = [None] * size
        self.head = 0
        self.tail = 0

def q_empty(queue):
    return queue.head == queue.tail

def q_full(queue):
    return (queue.tail + 1) % len(queue.data) == queue.head

def q_enque(queue, value):
    if not q_full(queue):
        queue.data[queue.tail] = value
        queue.tail = (queue.tail + 1) % len(queue.data)
    else:
        return "Error message"

def q_deque(queue):
    if not q_empty(queue):
        result = queue.data[queue.head]
        queue.data[queue.head] = None
        queue.head = (queue.head + 1) % len(queue.data)
        return result
    else:
        return "Error message"

s = Queue(5)
q_enque(s, 2)
q_enque(s, 4)
q_enque(s, 8)
print(f"{s.data} h:{s.head} t:{s.tail}\n")
print("Test 1 expects: 2")
print("Test 1 gets:    " + str(q_deque(s)))
print(f"{s.data} h:{s.head} t:{s.tail}\n")
print("Test 2 expects: 4")
print("Test 2 gets:    " + str(q_deque(s)))
print(f"{s.data} h:{s.head} t:{s.tail}\n")
print("Test 3 expects: 8")
print("Test 3 gets:    " + str(q_deque(s)))
print(f"{s.data} h:{s.head} t:{s.tail}\n")
print("Test 4 expects: Error message")
print("Test 4 gets:    " + str(q_deque(s)))
print(f"{s.data} h:{s.head} t:{s.tail}\n")