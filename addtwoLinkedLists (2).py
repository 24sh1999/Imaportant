class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next
            
    def print_helper(self, node, name):
        if node is None:
            print(name + ": None")
        else:
            print(name + ":" + node.data)

            

    def reverse_iterative(self):

        prev = None 
        cur = self.head
        while cur:
            nxt = cur.next
            cur.next = prev
            self.print_helper(prev, "PREV")
            self.print_helper(cur, "CUR")
            self.print_helper(nxt, "NXT")
            print("\n")

            prev = cur 
            cur = nxt 
        self.head = prev






    def append(self, data):
            new_node = Node(data)

            if self.head is None:
                self.head = new_node
                return

            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            last_node.next = new_node






    def sum_two_lists(self, llist):
            p = self.head
            print(p.data)
            q = llist.head
            print(q.data)

            sum_llist = LinkedList()

            carry = 0
            while p or q:
                if not p:
                    i = 0
                else:
                    i = p.data
                if not q:
                    j = 0 
                else:
                    j = q.data
                s = i + j + carry
                if s >= 10:
                    carry = 1
                    remainder = s % 10
                    sum_llist.append(remainder)
                else:
                    carry = 0
                    sum_llist.append(s)
                if p:
                    p = p.next
                if q:
                    q = q.next
            sum_llist.print_list()



llist1 = LinkedList()
llist1.append(5)
llist1.append(6)
llist1.append(3)

llist2 = LinkedList()
llist2.append(8)
llist2.append(4)
llist2.append(2)

llist1.sum_two_lists(llist2)
