class Solution:
    def averageValue(self, nums: List[int]) -> int:
        s,c=0,0
        for i in nums:
            if i%6==0:
                s+=i
                c+=1
        return s//c if c>0 else 0
