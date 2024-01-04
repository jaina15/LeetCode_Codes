class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = nums[0]+nums[1]+nums[2]
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            lo,hi=i+1,len(nums)-1
            while lo<hi:
                currSum = nums[i]+nums[lo]+nums[hi]
                if currSum == target:
                    return target
                if abs(currSum-target)<abs(result-target):
                    result = currSum
                if currSum<target:
                    lo+=1
                else:
                    hi-=1
        return result
