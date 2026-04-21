# Queue empty handling example

queue = []

try:
    queue.pop(0)
except IndexError:
    print("Cannot dequeue: Queue is empty.")

if queue:
    queue.pop(0)
else:
    print("Queue is empty, so dequeue is skipped.")
