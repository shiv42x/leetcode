# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        """
        create width of n length between 2 pointers
        when fast pointer reaches end, slow will be exactly 1 before node to be deleted (bcz of the dummy node)
        """
        
        dummy = ListNode(0)
        dummy.next = head
        
        fast = dummy
        slow = dummy
        
        for _ in range(n):
            fast = fast.next
            
        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return dummy.next