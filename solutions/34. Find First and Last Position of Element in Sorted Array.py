class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans=[-1,-1]
        start = self.search(nums, target, True)
        end = self.search(nums, target, False)
        ans[0], ans[1] = start, end
        return ans
​
    def search(self, nums, target, searchFirst):
        ans = -1
        start, end=0,len(nums)-1
        while start<=end:
            mid = start + (end-start)//2
            if target < nums[mid]:
                end = mid - 1
            elif target > nums[mid]:
                start = mid + 1
            else:
                ans = mid
                if searchFirst:
                    end = mid - 1
                else:
                    start = mid + 1
        return ans
