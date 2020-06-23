class ListNode(object):
        def __init__(self,x):
                self.val = x
                self.next = None
class Solution(object):
        
        def linked_list_str(l):
                    if l is None:
                        return ''
                    return str(l.val) + '->' + linked_list_str(l.next)
        def addTwoNumbers(self,l1,l2):
                print("")
                print('Inside Function')
		
		#Declare Pointers for traversal. Added for clarity.
                p1 = l1
                p2 = l2
                #Declare current carry over.
                currentCarry = 0
		#Declare cur variable to hel traverse and add nodes to new list.
		#Delcare head variable to be the head of the list.
                head = cur = ListNode(0)
                #Iteration Condition.
                while p1 or p2 or currentCarry:
                        print(p1.val, p2.val, currentCarry)
			
			#Determine current value and carry over.
                        currentVal = currentCarry
                        currentVal += 0 if p1 is None else p1.val
                        currentVal += 0 if p2 is None else p2.val
                        if currentVal >= 10:
                                currentVal -= 10
                                currentCarry = 1
                        
                        else:
                        	currentCarry = 0
                        print(currentVal,currentCarry)
			
			#Add current value as it will always atleast be '1'
                        
			
                        cur.next = ListNode(currentVal)
                        cur = cur.next
			
			#Add base case for iterating linked lists.
			
                        if p1 is None or p2 is None:
                        	break
                        elif p1 is None:
                        	p2 = p2.next
                        elif p2 is None:
                        	p2 = p2.next
                        print('existing....')
                        print("")
			#Return next node.
                        return head.next

		

		
                        
			
	
	#Recursively print linked list
        print("")
	#Make first linked list.
        l1 = ListNode(2)
        l1.next = ListNode(4)
        l1.next.next = ListNode(3)
        print(linked_list_str(l1))
	#Make second linked list
        l2 = listNode(5)
        l2.next = listNode(5)
        l2.next.next = listNode(5)
	#Add linked lists.
        s = Solution()
        l3 = s.addTwoNumbers(l1,l2)
        print(linked_list_str(l3))
        print("")


	
