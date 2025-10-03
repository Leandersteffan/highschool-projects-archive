# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a, b, c, d, e, is_a, a_val, b_val = [], [], [], 0, 0, True, '',''
        
        # Get values from sorted lists
        while True:
            try:
                a.append(l1.val)
            except AttributeError:
                break
            l1 = l1.next
        while True:
            try:
                b.append(l2.val)
            except AttributeError:
                break
            l2 = l2.next
            
        # create result
        a.reverse()
        for i in range(len(a)):
            a_val += str(a[i])
        b.reverse()
        for i in range(len(b)):
            b_val += str(b[i])
        d = int(b_val) + int(a_val)
        d = str(d)
        for i in range(len(d)):
            e = d[i]
            c.append(int(e))
            
        # create sorted list with result
        c.reverse()
        start = l3 = ListNode(val=c[0])
        for i in range(1, len(c)):
            l3.next = ListNode(val=c[i])
            l3 = l3.next
            
        return start
        
