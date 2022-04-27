class Stack:
    def __init__(self, size):
        self.data = [None] * size
        self.top = 0

def s_push(stack, value):
    return 42

def s_pop(stack):
    return 42

s = Stack(20)
s_push(s, 2)
s_push(s, 4)
s_push(s, 8)
print("Test 1 expects: 8")
print("Test 1 gets:    " + str(s_pop(s)))
print("Test 2 expects: 4")
print("Test 2 gets:    " + str(s_pop(s)))
print("Test 3 expects: 2")
print("Test 3 gets:    " + str(s_pop(s)))
print("Test 4 expects: Error message")
print("Test 4 gets:    " + str(s_pop(s)))