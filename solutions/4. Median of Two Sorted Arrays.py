class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1+nums2
        nums.sort()
        if len(nums)%2==0:
            m1 = len(nums)//2
            m2 = (len(nums)//2-1)
            return (nums[m1]+nums[m2])/2
        else:
            return nums[len(nums)//2]
