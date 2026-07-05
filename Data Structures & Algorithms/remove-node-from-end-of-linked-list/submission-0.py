# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        this is basically traversing a linked list
        however
        when we reach teh nth node
        we need to spin up a temp node to be the node in front of the nth node
        we disconnect the nth node and reconned the n-1th node to the n+1th node

        correction.. linked lists are always con=unted backwards...
        [1,2] n = 2 remove 1
        but we can't just index a linked list
        we will use two pointers
        [1,2,3,4,5,6,7] n = 1
        pointer1 = 0
        pointer2 = pointer1 + n
        increment both pointers until pointer2 hts null
        once pointer2 hits null pointer1 will be at the nth value
        then do the logic above
        """
        dummy = ListNode(0, head)
        pointer1, pointer2 = dummy, dummy

        for i in range(n):
            pointer2 = pointer2.next
        
        while pointer2.next:
            pointer1 = pointer1.next
            pointer2 = pointer2.next
        
        # now pointer1 will be at the n-1th value

        """
        [1,2,3,4,5,6,7] n = 3
                 p1     p2
        """
        pointer1.next = pointer1.next.next

        return dummy.next
