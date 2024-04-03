class Node(object):
    """Node class for reference"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
def get_nth(node, index):
    result = node
    depth = 0
    current = node
    while current:
        depth += 1
        current = current.next
    if index < 0 or index > depth-1:
        raise ValueError
    for _ in range(index):
        result = result.next
    return result