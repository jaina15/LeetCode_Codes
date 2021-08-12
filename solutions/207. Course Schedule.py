#just to remember yahan p ulti value return k h cycle mili isliyye false return kia warna true kia. main funnction k baat hori h.
from collections import defaultdict
class Solution:
    def canFinish(self, n: int, pre: List[List[int]]) -> bool:
        g=defaultdict(list)
        for i in range(len(pre)):
            g[pre[i][0]].append(pre[i][1])
            
        vis=[False]*n
        dfsVis=[False]*n
        
        for i in range(n):
            if not vis[i]:
                if self.checkCycle(i,g,vis,dfsVis):
                    return False
        print(vis,dfsVis)
        return True
    def checkCycle(self,node,g,vis,dfsVis):
        vis[node]=True
        dfsVis[node]=True
        for i in g[node]:
            if not vis[i]:
                if(self.checkCycle(i,g,vis,dfsVis)):
                    return True
            elif dfsVis[i]:
                return True
