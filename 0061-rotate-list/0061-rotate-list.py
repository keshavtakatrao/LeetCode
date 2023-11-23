# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head or not head.next or k == 0:
            return head
        
        
        nodeCount = 1
        current = head
        
        while current.next:
            nodeCount +=1
            current = current.next
            
        k = k % nodeCount
        
        
        if k==0:
            return head
        
        newTailIdx = nodeCount - k -1
        current = head
        
        for _ in range(newTailIdx):
            current = current.next
            
        newHead = current.next
        current.next = None
        
        current = newHead
        while current.next:
            current = current.next
        current.next = head
        
        return newHead
        
        