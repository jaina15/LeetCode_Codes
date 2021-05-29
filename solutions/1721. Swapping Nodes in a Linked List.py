#        temp=head
#        while temp:
#            l.append(temp.val)
#            temp=temp.next
#        a=l[k-1]
#        b=l[len(l)-k]
        #print(l)
        #print(a)
        #print(b)
#        l[k-1]=b
#        l[len(l)-k]=a
        #print(l)
#        head=ListNode()
#        for i in l:
#            new_node=ListNode(i)
#            
#            last=head
#             while last.next:
#                last=last.next
                
#            last.next=new_node
        
#        return head.next
​
​
# ye mere wale solution ka h optmized version h, isme mene list se ll banane k time me nested loop nhi use kia. Ye yaad rakhna h!!!!!
        l=[]
        temp=head
        while temp:
            l.append(temp.val)
            temp=temp.next
        a=l[k-1]
        b=l[len(l)-k]
        #print(l)
        #print(a)
        #print(b)
        l[k-1]=b
        l[len(l)-k]=a
        #print(l)
        head=dummy=ListNode()
        for i in l:
            dummy.next=ListNode(i)
            dummy=dummy.next
        
        return head.next
        
