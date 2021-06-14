class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        d={}
        
        for i in range(len(nums2)):
            while stack and nums2[stack[-1]]<=nums2[i]:
                d[nums2[stack[-1]]]=nums2[i]
                stack.pop()
            stack.append(i)
        #print(d)
        stack.clear()
        for i in range(len(nums1)):
            stack.append(d.get(nums1[i],-1))
        
        #print(stack)
        return stack
