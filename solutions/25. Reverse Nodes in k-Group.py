            temp=prev
            #k nodes k list banane k liye
            while n>1 and temp:
                temp=temp.next
                n-=1
            prev=temp.next
            temp.next=None
            #print(temp)
            #print(prev)
            #print(newhead)
            curr=newhead
            pr=None
            while curr:
                next=curr.next
                curr.next=pr
                pr=curr
                curr=next
            newhead=pr
            #print(newhead)
            while dummy.next:
                dummy=dummy.next
            dummy.next=newhead
            #print(ans.next)
            times-=1
        #print(prev)
        #ye jab hume left out nodes ko bina reverse kie add karna h
        if prev:
            while dummy.next:
                dummy=dummy.next
            dummy.next=prev
        return ans.next
