class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
    
def stringify(node):
    """
    Returns nodes into the string sequence.
    """
    if node is None:
        return 'None'
    result = ''
    while node.next:
        result += str(node.data)
        result += ' -> '
        node = node.next
    result += f'{str(node.data)} -> None'
    return result
