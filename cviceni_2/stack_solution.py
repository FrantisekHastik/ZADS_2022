class Stack:
    def __init__(self, size):
        self.data = [None] * size
        self.top = 0

def s_push(stack, value):
    if stack.top < len(stack.data):
        stack.data[stack.top] = value
        stack.top += 1
        return stack
    else:
        print("Cannot push onto full stack.")

def s_pop(stack):
    if stack.top > 0:
        stack.top -= 1
        return stack.data[stack.top]
    else:
        print("Cannot pop from empty stack.")

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