        
        if(la<=lb):
            tempa=headA
            tempb=headB
            while(tempa):
                s.add(tempa)
                tempa=tempa.next
            
            while(tempb):
                if(tempb in s):
                    return tempb
                tempb=tempb.next
​
        else:
            tempa=headA
            tempb=headB
            while(tempb):
                s.add(tempb)
                tempb=tempb.next
            
            while(tempa):
                if(tempa in s):
                    return tempa
                tempa=tempa.next
                
        return None
    
 #better and optimized solution. Think like this Shubham!!!   
    #def getIntersectionNode(self, headA, headB):
    #    if headA is None or headB is None:
    #        return None
​
    #    pa = headA # 2 pointers
    #    pb = headB
​
    #    while pa is not pb:
    #        # if either pointer hits the end, switch head and continue the second traversal, 
    #        # if not hit the end, just move on to next
    #        pa = headB if pa is None else pa.next
    #        pb = headA if pb is None else pb.next
​
     #   return pa # only 2 ways to get out of the loop, they meet or the both hit the end=None
​
# the idea is if you switch head, the possible difference between length would be countered. 
# On the second traversal, they either hit or miss. 
# if they meet, pa or pb would be the node we are looking for, 
# if they didn't meet, they will hit the end at the same iteration, pa == pb == None, return either one of them is the same,None
