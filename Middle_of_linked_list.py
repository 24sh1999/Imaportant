class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        s = head
        q = head
        while(q.next):
            s = s.next
            q = q.next
            if not q.next: # quick pointer empty, even number of link nodes
                return s
            q = q.next
            
        return s
