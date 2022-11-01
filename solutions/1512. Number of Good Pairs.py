class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ans=0
        d=dict()
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        
        for k,v in d.items():
            ans+=(v*(v-1))//2
        return ans
