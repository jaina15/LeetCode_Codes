class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = nums[0] + nums[1] + nums[2]
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
​
            l, r = i + 1, len(nums) - 1
            while l < r:
                curSum = nums[l] + nums[r] + nums[i]
                if curSum == target:
                    return target
                if abs(curSum-target) < abs(result-target):
                    result = curSum
                if curSum < target:
                    l += 1
                else:
                    r -= 1
        return result
