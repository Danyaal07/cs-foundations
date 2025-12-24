stack = []

def push(stack, val):
    stack.append(val)

def pop(stack):
    if stack:
        return stack.pop()
    return None

def peek(stack):
    if stack:
        return stack[-1]
    return None

def is_empty(stack):
    return not stack

push(stack, 10)
push(stack, 20)
print(pop(stack))
print(peek(stack))
print(is_empty(stack))