from collections import defaultdict
import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph=defaultdict(list)
        for u,v,w in flights:
            graph[u].append((v,w))
        k=k+1
        heap=[(0,src,k)]
        seen=dict()
        #visited=[-1]*n
        while heap:
            #print(heap)
            cost,node,stops=heapq.heappop(heap)
            #print(cost,node,stops)
            if node==dst:
                return cost
            if node in seen and seen[node]>=stops:
                continue
            seen[node]=stops
            #if stops<=0:
            #    print('hello')
            #    continue
            #if visited[node]!=-1 and cost>visited[node]:
            #    continue
            #if cost<visited[node]:
            #    visited[node]=cost
            #print(visited)
            if stops:
                for v,w in graph[node]:
                    heapq.heappush(heap,(cost+w,v,stops-1))
            #k-=1
        #print(visited)
        #return visited[dst]
        return -1
