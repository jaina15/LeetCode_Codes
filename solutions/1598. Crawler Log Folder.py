class Solution:
    def minOperations(self, logs: List[str]) -> int:
        ans = 0
        for i in logs:
            if i == '../':
                if ans>0:
                    ans-=1
            elif i != './':
                ans+=1
        return ans
