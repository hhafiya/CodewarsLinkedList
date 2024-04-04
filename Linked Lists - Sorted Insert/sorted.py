class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f'Node{self.data, self.next}'

def sorted_insert(head, data):
    current = head
    if head is None:
        return Node(data)
    if head.data > data:
        new_node = Node(data)
        new_node.next = head
        return new_node
    while current is not None:
        if current.next is None:
            new_node = Node(data)
            current.next = new_node
            return head
        if current.data < data and current.next.data > data:
            new_node = Node(data)
            new_node.next = current.next
            current.next = new_node
            return head
        else:
            current = current.next
