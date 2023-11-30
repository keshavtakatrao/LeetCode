# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = ""
        num2 = ""
        
        current  = l1
        
        while current:
            num1 = str(current.val) + num1
            current = current.next
            
        current  = l2
        
        while current:
            num2 = str(current.val) + num2
            current = current.next
            
            
        sumCount = str(int(num1) + int(num2))[::-1]  

        dummy = ListNode()
        current = dummy

        for digit in sumCount:
            current.next = ListNode(int(digit))
            current = current.next

        return dummy.next