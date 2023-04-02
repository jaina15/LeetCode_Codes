​
    def addAtTail(self, val: int) -> None:
        curr=self.head
        if curr is None:
            self.head=Node(val)
        else:
            while curr.next:
                curr=curr.next
            curr.next=Node(val)
        self.size+=1
        
    def addAtIndex(self, index: int, val: int) -> None:
        if index<0 or index>self.size:
            return
        if index==0:
            self.addAtHead(val)
        else:
            node=Node(val)
            curr=self.head
            for i in range(index-1):
                curr=curr.next
            node.next=curr.next
            curr.next=node
            self.size+=1
        
    def deleteAtIndex(self, index: int) -> None:
        if index<0 or index>=self.size:
            return
        if index==0:
            self.head=self.head.next
        else:
            curr=self.head
            for i in range(index-1):
                curr=curr.next
            curr.next=curr.next.next
        self.size-=1
​
​
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
