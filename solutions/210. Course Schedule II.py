from collections import defaultdict
class Solution:
    def findOrder(self, n: int, pre: List[List[int]]) -> List[int]:
        g=defaultdict(list)
        for i in range(len(pre)):
            g[pre[i][0]].append(pre[i][1])
        #print(g)
        stack=[]
        vis=[False]*n
        dfsVis=[False]*n
        for i in range(n):
            if not vis[i]:
                if self.checkCycle(i,g,vis,dfsVis,stack):
                    #print(vis,dfsVis)
                    return []
        #print(vis,dfsVis)
        return stack
    
    def checkCycle(self,node,g,vis,dfsVis,stack):
        vis[node]=True
        dfsVis[node]=True
        for i in g[node]:
            if not vis[i]:
                if self.checkCycle(i,g,vis,dfsVis,stack):
                    return True
            elif dfsVis[i]:
                return True
        dfsVis[node]=False
        stack.append(node)
        return False
    #def topSort(self,node,g,vis,stack):
    #    vis[node]=True
    #    for i in g[node]:
    #        if not vis[i]:
    #            self.topSort(i,g,vis,stack)
    #    stack.append(node)
