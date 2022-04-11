# class Node:
#     def __init__(self,data=None,next=None):
#         self.data=data
#         self.next=next
#
# class LinkedList:
#     def __init__(self):
#         self.head=None
#
#     def print(self):
#         if self.head is None:
#             print("My linked List is empty")
#             return
#         n = self.head
#         llstr = ' '
#         while n is not None:
#             llstr +=str(n.data) + "--->" if n.next else str(n.data)
#             n=n.next
#         print(llstr)
#     def add_beg(self,data):
#         new_node = Node(data,self.head)
#         self.head = new_node
#
#     def add_end(self,data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head=new_node
#         else:
#             n=self.head
#             while n.next is not None:
#                 n = n.next
#             n.next = new_node
#     def after_node(self,data,x):
#         n = self.head
#         while self.head is None:
#             if x==n.data:
#                 break
#             n=n.next
#         if n is None:
#             print(" node is not present in ll")
#         else:
#             new_node = Node(data)
#             new_node.next = n.next
#             n.next = new_node

class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
class Linkedlist:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("My linkedlist is empty")
            return
        n = self.head
        llstr = ''
        while n is not None:
            llstr += str(n.data) + "--->"
            n=n.next
        print(llstr)

    def add_beg(self,data):
        new_node = Node(data,self.head)
        self.head = new_node

    def add_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        n = self.head
        while n.next is not None:
            n= n.next
        n.next= Node(data)










if __name__=="__main__":
    ll=Linkedlist()
    ll.add_beg(100)
    ll.add_beg(200)
    ll.add_at_end(400)
    ll.print()

