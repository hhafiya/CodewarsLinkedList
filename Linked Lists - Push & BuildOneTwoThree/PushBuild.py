
'''
Node is defined in preloaded like this:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
    
def push(head, data):
    pushed = Node(data)
    pushed.next = head
    return pushed

def build_one_two_three():
    lst = [3, 2, 1]
    head = None
    for data in lst:
        head = push(head, data)