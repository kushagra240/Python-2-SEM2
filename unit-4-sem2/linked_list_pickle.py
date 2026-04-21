import pickle


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def write_linked_list_with_pickle(head, filename):
    with open(filename, 'wb') as file:
        pickle.dump(head, file)


def restore_linked_list_with_pickle(filename):
    with open(filename, 'rb') as file:
        head = pickle.load(file)
    return head


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
write_linked_list_with_pickle(head, 'linked_list.pkl')

restored_head = restore_linked_list_with_pickle('linked_list.pkl')
