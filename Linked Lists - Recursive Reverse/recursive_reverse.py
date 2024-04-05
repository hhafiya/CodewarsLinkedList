class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
    def __repr__(self):
        return f'Node{self.data, self.next}'


def reverse(head):
    if head is None or head.next is None:
        return head
    reversed_head = reverse(head.next)
    head.next.next = head
    head.next = None
    return reversed_head


node_1 = Node(2)
node_2 = Node(3)
node_3 = Node(5)
node_4 = Node(6)
node_5 = Node(11)
node_1.next = node_2
node_2.next = node_3
node_3.next = node_4
node_4.next = node_5
print(reverse(node_1))