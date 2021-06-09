class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        # ye mene dekha h youtube se
        stack=[]
        left_min=[]
        left_min.append(nums[0])
        for i in range(1,len(nums)):
            left_min.append(min(left_min[i-1],nums[i]))
        
        for j in range(len(nums)-1,-1,-1):
            if nums[j]>left_min[j]:
                while stack and stack[-1]<=left_min[j]:
                    stack.pop()
                if stack and stack[-1]<nums[j]:
                    return True
                stack.append(nums[j])
        #print(left_min)
        return False
