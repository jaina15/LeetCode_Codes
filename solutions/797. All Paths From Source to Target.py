from collections import defaultdict
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        g=defaultdict(list)
        self.V=len(graph)
        for i in range(len(graph)):
            for j in range(len(graph[i])):
                g[i].append(graph[i][j])
        
        #print(g)
        self.ans=[]
        self.dfs(g,0,len(graph)-1)
        return self.ans
    
    def dfs(self,g,s,d):
        visited=[False]*self.V
        path=[]
        self.allPath(g,s,d,visited,path)
    
    def allPath(self,g,s,d,visited,path):
        visited[s]=True
        path.append(s)
        if s==d:
            #print(path)
            self.ans.append(path.copy())
            #print(self.ans)
        else:
            for i in g[s]:
                if visited[i]==False:
                    self.allPath(g,i,d,visited,path)
        
        path.pop()
        visited[s]=False    
