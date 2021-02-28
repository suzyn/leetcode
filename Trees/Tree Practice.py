class Node : 
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None

class BinaryTree() :
    # 트리생성
    def __init__(self):
        self.root = None
    
    # 전위순회 (root-left-right)
    def preorder(self,n):
        if n != None:
            print(n.item,' ',end='')     # 노드방문 
            if n.left:
                self.preorder(n.left)   # 왼쪽 서브트리 순회 
            if n.right:
                self.preorder(n.right)  # 오른쪽 서브트리 순회 
    
    # 중위순회 (left-root-right)
    def inorder(self,n):
        if n!=None:
            if n.left:
                self.inorder(n.left)   # 왼쪽 서브트리 순회 
            print(n.item,' ',end='')   # 노드 방문
            if n.right:
                self.inorder(n.right)  # 오른쪽 서브트리 순회 
    # 후위 순회 (left-right-root)
    def postorder(self,n):
        if n!=None : 
            if n.left:
                self.postorder(n.left)   # 왼쪽 서브트리 순회 
            if n.right:
                self.postorder(n.right)  # 오른쪽 서브트리 순회 
            print(n.item,' ', end='')   # 노드 방문

    # 레벨 순회 
    def levelorder(self, root):
        q = []      # 큐로 이용할 리스트 선언
        q.append(root)
        while q:
            t=q.pop(0)
            print(t.item, ' ', end='')   # 큐에서 첫번째 항목 삭제 후 삭제한 노드 방문
            if t.left != None:
                q.append(t.left)         # 왼쪽 자식을 큐에 삽입 
            if t.right != None:
                q.append(t.right)        # 오른쪽 자식울 큐에 삽입 
    
    def height(self, root):
        if root == None:
            return 0
        # 루트 노드를 기준으로 두 자식노드의 높이 중 큰 높이 
        return max(self.height(root.left), self.height(root.right))+1

tree=BinaryTree()
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)
n5 = Node(50)
n6 = Node(60)
n7 = Node(70)
n8 = Node(80)

# 트리 만들기 
tree.root=  n1
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7
n4.left = n8

# 트리높이
print('트리높이 : ', tree.height(tree.root))

# 전위순회
print('전위순회 : ', end='')
tree.preorder(tree.root)

# 중위순회
print('\n중위순회 : ', end='')
tree.inorder(tree.root)

# 후위순회
print('\n후위순회 : ', end='')
tree.postorder(tree.root)

# 레벨순회
print('\n레벨순회 : ', end='')
tree.levelorder(tree.root)

# 출처
    # https://it-garden.tistory.com/406
    # http://blog.naver.com/PostView.nhn?blogId=leeinje66&logNo=221622228795