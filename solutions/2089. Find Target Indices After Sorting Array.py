class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        first = self.firstOccurrence(nums,target)
        last = self.lastOccurrence(nums,target)
        if first == -1:
            return []
        else:
            return range(first,last+1)
        
    def firstOccurrence(self, nums, target):
        low,high = 0, len(nums)-1
        while low<=high:
            mid = (low+high)//2
            if nums[mid]<target:
                low = mid + 1
            elif nums[mid]>target:
                high = mid - 1
            else:
                if mid == 0 or nums[mid]!=nums[mid-1]:
                    return mid
                else:
                    high = mid - 1
        return -1
    
    def lastOccurrence(self, nums, target):
        low,high = 0, len(nums)-1
        while low<=high:
            mid = (low+high)//2
            if nums[mid]<target:
                low = mid + 1
            elif nums[mid]>target:
                high = mid - 1
            else:
                if mid == len(nums)-1 or nums[mid]!=nums[mid+1]:
                    return mid
                else:
