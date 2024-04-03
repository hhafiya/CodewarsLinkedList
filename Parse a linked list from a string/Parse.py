class Node:
    def __init__(self, data, next=None): 
        self.data = data
        self.next = next

def linked_list_from_string(s):
    s_list = list(reversed(s.split(' -> ')))
    tail, s_list = None, s_list[1:]
    current, head = tail, None
    for i in s_list:
        head = Node(int(i), current)
        current = head
    return head
