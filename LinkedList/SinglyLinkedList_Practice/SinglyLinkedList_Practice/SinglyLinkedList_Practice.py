# Node 클래스 선언 
class Node(object) : 
    def __init__(self,data):
        self.data=data
        self.next=None

# Singly Linked List 클래스 선언 
class SinglyLinkedList(object) : 
    def __init__(self):
        self.head=None
        self.count=0

    # Add new node at the end of the linked list 
    def append(self,node):
        if self.head==None:
            self.head=node
        else:
            cur=self.head
            # Move 'cur' to the end of the linked list 
            while cur.next!=None:
                cur=cur.next
            cur.next=node
        
    # Return (first) index of data in the linked list 
    def getDataIndex(self, data):
        cur=self.head
        idx=0
        # while cur!=None
        while cur:
            if cur.data==data:
                return idx
            cur=cur.next
            idx+=1
        return -1

    # Add new node at the given index
    def insertNodeAtIndex(self, idx, node):
        '''
        Node can be added in 3 ways
        (1) At the front of the linked list
        (2) At the given index
        (3) At the end of the linked list 
        '''
        cur = self.head 
        prev=None
        cur_i=0

        # (1) Add node at the front
        if idx==0:
            # if not empty
            if self.head:
                next=self.head
                self.head=node
                self.head.next=next
            # if empty
            else:
                self.head=node
        # (2) Add at the given index
        # (3) Add at the end of the linked list 
        else:
            # Move 'cur' to the given index 
            while cur_i<idx:
                if cur:
                    prev=cur
                    cur=cur.next
                else:
                    break
                cur_i+=1
            if cur_i==idx:
                node.next=cur
                prev.next=node
            else:
                return -1

    # Clear Linked List 
    def clear(self):
        self.head=None

    # Print 
    def print(self):
        cur=self.head 
        string=""
        while cur:
            string +=str(cur.data)
            if cur.next:
                string+="->"
            cur=cur.next
        print(string)


if __name__=="__main__":

    sl=SinglyLinkedList()
    sl.append(Node(1))
    sl.append(Node(2))
    sl.append(Node(3))
    sl.append(Node(5))
    sl.insertNodeAtIndex(3, Node(4))
    print("Singly Linked List : ")
    sl.print()

    print("\nData Index : ")
    print(sl.getDataIndex(1))
    print(sl.getDataIndex(2))
    print(sl.getDataIndex(3))
    print(sl.getDataIndex(4))
    print(sl.getDataIndex(5))

    sl.insertNodeAtIndex(1, Node(0))
    print("\nUpdated Singly Linked List : ")
    sl.print()