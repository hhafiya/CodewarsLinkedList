class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __repr__(self):
        return f'Node{self.data, self.next}'

    
def push(head, data):
    pushed = Node(data)
    pushed.next = head
    return pushed

def build_one_two_three():
    lst = [3, 2, 1]
    head = None
    for data in lst:
        head = push(head, data)
    return head
