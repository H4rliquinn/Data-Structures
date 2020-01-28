class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def add(self, value):
        self.next = Node(value)


def reverse_ll(ll):
    while node.next:
        save = ll
        ll = ll.next
        ll.next = save
        ll.next.next = ll.next.next
