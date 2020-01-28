

class SingleLinkedList:
    def __init__(self, node=None):
        self.head = node

    def add_to_tail(self, value):
        new_node = ListNode(value, None)
        if not self.head:
            self.head = new_node


class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


ll = SingleLinkedList(ListNode(5))
ll.add_to_tail(6)
ll.add_to_tail(2)
print(ll.head.value, ll.head.next.value)


def check_half(ll):
    # starts both counters
    counter = ll.head
    half = ll.head

    # returns none if linked list is empty
    if counter is None:
        return(None)

    # returns the head if it is the only node
    elif counter.next is None:
        return(counter)

    # otherwise begin the counter loop
    else:
        counting = 1
        while counting == 1:
            counter = counter.next
            if counter is not None:
                if counter.next is None:
                    counting = 0
                else:
                    counter = counter.next
                    half = half.next
        return half
