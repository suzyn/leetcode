#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        # control empty lists
        if(l1==None) : return l2
        if(l2==None) : return l1
        
        # define start point (head)
        head=None
        if(l1.val<=l2.val):
            head=l1
            l1=l1.next
        else:
            head=l2
            l2=l2.next
        
        # connect lists
        l3_cur=head
        while(l1 and l2):
            if(l1.val<=l2.val):
                l3_cur.next=l1
                l3_cur=l3_cur.next
                l1=l1.next
            else:
                l3_cur.next=l2
                l3_cur=l3_cur.next
                l2=l2.next
        
        # 아직 None에 도달하지 않은 리스트를 연결 
        if(l1) : l3_cur.next=l1
        else   : l3_cur.next=l2
            
        return head
        