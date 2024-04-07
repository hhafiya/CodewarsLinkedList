class Node:
    def __init__(self, data, next=None): 
        self.data = data
        self.next = next

    def __repr__(self):
        return f'Node{self.data, self.next}'
    
def swap_pairs(head):
    if not head or not head.next:
        return head
    temp = Node(-1)
    temp.next = head
    prev = temp
    while prev.next and prev.next.next:
        first = prev.next
        second = prev.next.next
        prev.next = second
        first.next = second.next
        second.next = first
        prev = first
    return temp.next
head = Node(1, Node(2, Node(3, Node(4))))
print(swap_pairs(head))