class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = self.firstOccurrence(nums,target)
        last = self.lastOccurrence(nums,target)
        return [first,last]
    
    def firstOccurrence(self,nums,target):
        low=0
        high=len(nums)-1
        
        while low<=high:
            mid = (low+high)//2
            if nums[mid]<target:
                low = mid+1
            elif nums[mid]>target:
                high = mid-1
            else:
                if mid==0 or nums[mid]!=nums[mid-1]:
                    return mid
                else:
                    high=mid-1
        return -1
    
    def lastOccurrence(self,nums,target):
        low=0
        high=len(nums)-1
        
        while low<=high:
            mid = (low+high)//2
            if nums[mid]<target:
                low = mid+1
            elif nums[mid]>target:
                high = mid-1
            else:
                if mid==len(nums)-1 or nums[mid]!=nums[mid+1]:
                    return mid
                else:
                    low=mid+1
        return -1
