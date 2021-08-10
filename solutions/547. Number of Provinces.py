from collections import defaultdict
class Solution:
    cnt=0
    def findCircleNum(self, c: List[List[int]]) -> int:
        g = defaultdict(list)
        for i in range(len(c)):
            for j in range(len(c[i])):
                if c[i][j]== 1:
                    g[i].append(j)
        #print(g)
        self.visited=[False]*len(g)
        self.component=[-1]*len(g)
        self.dfs(0,g)
        for i in range(len(g)):
            if not self.visited[i]:
                self.cnt+=1
                self.dfs(i,g)
        #print(self.cnt)
        #print(self.component)
        #return len(set(self.component))
        return self.cnt+1
        
    def dfs(self,v,g):
        self.visited[v]=True
        self.component[v]=self.cnt
        for neighbour in g[v]:
            if not self.visited[neighbour]:
                self.dfs(neighbour,g)
    
