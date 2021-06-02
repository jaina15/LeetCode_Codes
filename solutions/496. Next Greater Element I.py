class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # dekh k kia h :(
        stack=[]
        lookup={}
        
        for i in nums2:
            if len(stack)==0:
                stack.append(i)
            elif i>stack[-1] and stack:
                while stack and i>stack[-1]:
                    lookup[stack.pop()]=i
                stack.append(i)
            else:
                stack.append(i)
        
        #print(lookup)
        ans=[]
        for i in nums1:
            ans.append(lookup.get(i,-1))
        
        return ans
        
