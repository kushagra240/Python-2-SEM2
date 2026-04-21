class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Linked List to File
def write_linked_list_to_file(head, filename):
    with open(filename, 'w') as file:
        current = head
        while current:
            file.write(f"{current.data}\n")
            current = current.next


# Example usage
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
write_linked_list_to_file(head, 'linked_list.txt')
