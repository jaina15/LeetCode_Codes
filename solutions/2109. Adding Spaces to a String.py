class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans=''
        for i in range(len(spaces)):
            if i==0:
                #print(s[0:spaces[i]])
                ans+=s[0:spaces[i]]+" "
            else:
                #print(s[spaces[i-1]:spaces[i]])
                ans+=s[spaces[i-1]:spaces[i]]+" "
        #print(s[spaces[i]:])
        ans+=s[spaces[i]:]
        return ans
