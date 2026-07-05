# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        lets try doing this but reverseing the linked list instead
        okay reversring a linked list
        we need a previous, a current and a temp

        --> 1 --> 2 --> 3 --> 4 --> Null
            p     c     t

        we want to take curr.next = prev
        then prev becomes curr
        and curr becomes temp
        and temp becomes curr.next
        """

        previous = None
        current = head
        while current:
            temp = current.next
            current.next = previous
            previous = current
            current = temp
        
        # now the linked list has reversed
        
        dummy = ListNode(0, previous) # note what when we reverse a linked list previous becomes the new previous
        # 1 --> 2 --> 3 --> 4 ... n = 2
        # dummy --> 4 --> 3 --> 2 --> 1 ... n = 2
        pointer1 = dummy
        # pointer2 = dummy.next
        for i in range(n - 1):
            pointer1 = pointer1.next
            # pointer2 = pointer2.next
        # now at this point pointer 1 should be on the n-1th node
        pointer1.next = pointer1.next.next


        # Reverse it back to the original order
        prev_back = None
        curr_back = dummy.next  # Start at the head of your modified list
        while curr_back:
            temp = curr_back.next
            curr_back.next = prev_back
            prev_back = curr_back
            curr_back = temp
            
        return prev_back  # This will be node 1, the true original head!
        return prev_back

