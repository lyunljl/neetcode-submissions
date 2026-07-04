# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        we will have a varaible track when the lists ends
        so while current: aka is still a node
        we will have previous be behind current
        1 --> 2 --> 3
        p     c     t

        """
        
        previous = None
        current = head
        while current:
            temp = current.next
            current.next = previous
            previous = current
            current = temp
        return previous
            
            
