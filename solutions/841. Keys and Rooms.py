from collections import defaultdict
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        g=defaultdict(list)
        for i in range(len(rooms)):
            for j in range(len(rooms[i])):
                g[i].append(rooms[i][j])
        #print(g)
        self.V=len(rooms)
        #print(self.V)
        return self.dfs(0,g)
        
    def dfs(self,v,g):
        visited=[False]*self.V
        self.dfsUtil(v,visited,g)
        #print(visited)
        if any(i==False for i in visited):
            return False
        return True
    
    def dfsUtil(self,v,visited,g):
        visited[v]=True
        for neighbour in g[v]:
            if visited[neighbour]==False:
                self.dfsUtil(neighbour,visited,g)
