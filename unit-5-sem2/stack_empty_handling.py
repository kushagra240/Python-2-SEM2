# Stack empty handling example

stack = []

try:
    stack.pop()
except IndexError:
    print("Cannot pop: Stack is empty.")

if stack:
    stack.pop()
else:
    print("Stack is empty, so pop is skipped.")
