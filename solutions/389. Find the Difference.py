class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        #d=dict()
        #for i in t:
        #    if i in d:
        #        d[i]+=1
        #    else:
        #        d[i]=1
        #for i in s:
        #    if i in d:
        #        d[i]-=1
        #for k,v in d.items():
        #    if v==1:
        #        return k
        ans=0
        for i in t:
            ans^=ord(i)
        for i in s:
            ans^=ord(i)
        return chr(ans)
