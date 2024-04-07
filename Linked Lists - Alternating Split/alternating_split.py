class Node(object):
    def __init__(self, data=None, next = None):
        self.data = data
        self.next = next

    def __repr__(self):
        return f'Node{self.data, self.next}'
    
class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
    def __repr__(self):
        return f'{self.first, self.second}'

def alternating_split(head):
    if head.next is None:
        raise ValueError
    first_head = head
    second_head = head.next

    current_first = first_head
    current_second = second_head

    while current_first and current_second and current_second.next:
        current_first.next = current_second.next
        current_first = current_first.next
        current_second.next = current_second.next.next
        current_second = current_second.next

    current_first.next = None
    if current_second:
        current_second.next = None
    return Context(first_head, second_head)


