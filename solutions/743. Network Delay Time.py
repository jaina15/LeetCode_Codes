from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        #pushed src node in the heapq with 0 distance as min dist from src to src is 0.
        heap=[(0,k)]
        #appended 0 at the start to make indexing one based as per the question
        distance=[0]+[float('inf')]*n
        while heap:
            #getting cost and the node
            time,node=heapq.heappop(heap)
            #comparing if we already have a minimum distance for this node which is visited through some other path
            if time<distance[node]:
                #setting the minimum time/cost to the node distance
                distance[node]=time
                #traversing this node to get further paths from here
                for j,w in graph[node]:
                    #pushing further nodes by incrementing distance traversed til now + the nodes distance from the last node to the heapq so that we can traverse them further
                    heapq.heappush(heap,(time+w,j))
        
        #print(distance)
        if max(distance)<float('inf'):
            return max(distance)
        return -1
                
