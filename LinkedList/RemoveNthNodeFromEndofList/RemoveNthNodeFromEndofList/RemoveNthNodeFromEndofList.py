# 이동 수 = (전체 노드 수)-(n)

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # Approach1: 28 ms, 14 MB
        
        # count the number of node
        cur=head
        count=0
        while cur:
            count+=1
            cur=cur.next

        # remove nth node
        cur=head
        prev=head        
        if(count==n):
            if(cur.next==None):head=None       # 리스트에 원소가 하나인 경우 
            else:head=cur.next                 # 리스트에 원소가 하나가 아닌 경우 
        else:
            for i in range(count-n):           # 'cur'을 n번째 노트로 이동시키기
                prev=cur
                cur=cur.next
            prev.next=cur.next
        
        return head
