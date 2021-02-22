# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool: 
        
        
        # Approach1 : bad solution (52 ms, 17.3MB)
            # 리스트의 값을 -10^5-1 (허용 범위를 벗어나는 값) 으로 바꾸면서 이동
            # 만약 -10^5-1을 만난다면, 해당 리스트는 사이클이 있는 리스트임
        if(head==None):
            return False
        else : 
            p1=head
            while(p1.next):
                p1.val=(-10^5-1)
                p1=p1.next
                if(p1.val==(-10^5-1)):return True

            return False
        
        # Approach2 : two-pointer (40ms, 17.7MB)
            # 빠르게 움직이는 포인터와 느리게 움직이는 포인터를 만듦 
            # 순회를 하면 할수록 차이가 1 만큼 벌어지기 때문에, cycle 내부에서 무조건 slower와 faster는 만나게 됨
        p1=head
        p2=head
        
        while(p1 and p2 and p2.next):
            p1=p1.next
            p2=p2.next.next 
            if(p1==p2):return True
        
        return False

        
        
        
        
        
