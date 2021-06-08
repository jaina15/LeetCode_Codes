        #print(stack[-2])
        #res=pos=0
        #if len(stack)==1:
        #    res=stack[-1]
        #    pos=k%len(stack[-1])
        #else:
        #    res=stack[-2]
        #    pos=k%len(stack[-2])
        #    
        #print(pos)
        #return res[pos-1]
        
        #solution s dekha, but isme stack to use h nhi kia inhone
        size=0
        for i in s:
            if i.isdigit():
                size*=int(i)
            else:
                size+=1
        
        for i in reversed(s):
            k=k%size
            if k==0 and i.isalpha():
                return i
            
            if i.isdigit():
                size/=int(i)
            else:
                size-=1
        
