"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        
        current = head
        
        while current:
            copy_node = Node(current.val)
            copy_node.next = current.next
            current.next = copy_node
            current = copy_node.next
            
        current = head
        while current:
            if current.random:
                current.next.random = current.random.next
            current = current.next.next
            
        new_head = head.next
        current = head
        while current:
            copy_node = current.next
            current.next = copy_node.next
            current = current.next
            if current:
                copy_node.next = current.next

        return new_head