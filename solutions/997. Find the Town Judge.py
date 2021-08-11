from collections import defaultdict
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if not trust and n>1:
            return -1
        g=defaultdict(list)
        for i in range(len(trust)):
            g[trust[i][0]].append(trust[i][1])
        
        s=set(range(1,n+1))
        ss=set(key for key, val in g.items())
        l=list(s-ss)
        c=0
        for i in g:
            if l==g[i] or set(l)<=set(g[i]):
                c+=1
        if not l or c!=len(g):
            return -1
        return l[0]
        
        
        
