class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def __repr__(self):
        return f'Node{self.data}'

def loop_size(node):
    slow = node
    fast = node
    loop = False
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            loop = True
            break
    if not loop:
        return 0
    start = node
    while start != slow:
        start = start.next
    size = 1
    current = start.next
    while current != start:
        size += 1
        current = current.next
    return size
