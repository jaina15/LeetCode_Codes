class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l=[]
        s=0
        e=len(nums)-1
        while s<e:
            test=nums[s]+nums[e]
            if test==target:
                l.append(s+1)
                l.append(e+1)
            if test<target:
                s+=1
            else:
                e-=1
        return l
        
