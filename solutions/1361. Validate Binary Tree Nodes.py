from collections import deque as queue
class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        root=0
        children=set(leftChild+rightChild)
        for i in range(n):
            if i not in children:
                root=i
                break
        visited=set()
        q=queue([root])
        
        while len(q)>0:
            curr=q.popleft()
            if curr in visited:
                return False
            visited.add(curr)
            
            if leftChild[curr]!=-1:
                q.append(leftChild[curr])
            if rightChild[curr]!=-1:
                q.append(rightChild[curr])
        
        if n!=len(visited):
            return False
        return True
