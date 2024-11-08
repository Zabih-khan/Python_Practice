class Node :
    def __init__(self,data):
        self.data=data
        self.next=None

class sll:
    def __init__(self):
        self.head=None

    def display(self):
        temp=self.head
        if self.head is None:
                print('Linked list is empty:')
        while temp:
            suffix=''
            if temp.next:
                suffix='-->'
            print(temp.data,suffix,end='')
            temp=temp.next
            

L=sll()
n1=Node(10)
L.head=n1
n2=Node(20)
n1.next=n2
n3=Node(30)
n2.next=n3
L.display()
