class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return head
        
        while head.val == val:
            if head.next: 
                head = head.next
            else: 
                if head.val == val: 
                    return None
                else:
                    return head
        
        head_pointer = head 
        
        while head.next:
            if head.next.val == val:
                #Set head.next to the next non-val node
                if head.next.next: 
                    lookahead_node = head.next.next
                else: 
                    head.next = None 
                    return head_pointer
                    
                while lookahead_node.val == val:
                    if lookahead_node.next: 
                        lookahead_node = lookahead_node.next
                    else: 
                        head.next = None
                        return head_pointer
                
                head.next = lookahead_node
                head = head.next
            else: 
                head = head.next
        
        return head_pointer