class Node:
    def __init__(self,data=None,next=None): # next is the pointer tot the next element
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self):
        self.head=None

    def insert_at_beg(self,data):
        node = Node(data,self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("My linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr+=str(itr.data) + "--->"
            itr=itr.next
        print(llstr)

    def insert_at_end(self,data):
        if self.head is None:
            self.head= Node(data,None)
            return
        itr =self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(data,None)

    def values(self,data_list):
        if self.head is None:
            for data in data_list:
                self.insert_at_end(data)

    def length(self):
        count=0
        itr= self.head
        while itr:
            count+=1
            itr=itr.next
        return count

    def remove_at(self,index):
        if index == 0:
            self.head=self.head.next
            return
        count=0
        itr = self.head
        while itr:
            if count==index-1:
                itr.next=itr.next.next
                break
            itr=itr.next
            count+=1
    def insert_at(self,index,data):
        if index==0:
            self.insert_at_beg(data)
            return
        count=0
        itr=self.head
        while itr:
            if count==index-1:
                node=Node(data,itr.next)
                itr.next=node
                break
            itr=itr.next
            count+=1

    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            return
        if self.head.data == data_after:
            self.head.next = Node(data_to_insert, self.head.next)
            return
        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert, itr.next)
                break
            itr = itr.next

    def remove(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        itr = self.head
        while itr:
            if itr.next.data == data:
                itr.next = itr.next.next


if __name__=="__main__":
    ll=LinkedList()
    ll.values(['banana','apple','jackfruit','orange'])

    ll.insert_at(1,"fig")
    ll.print()



