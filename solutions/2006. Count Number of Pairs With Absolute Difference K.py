class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        c=0
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        
        for i in nums:
            if i+k in d:
                c+=d[i+k]
        return c
