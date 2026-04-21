class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def restore_linked_list_from_file(filename):
    head = None
    current = None
    with open(filename, 'r') as file:
        for line in file:
            data = int(line.strip())
            new_node = Node(data)
            if not head:
                head = new_node
                current = head
            else:
                current.next = new_node
                current = current.next
    return head


def print_list(head):
    current = head
    while current:
        print(current.data, end=" ")
        current = current.next


restored_head = restore_linked_list_from_file('linked_list.txt')
print_list(restored_head)
