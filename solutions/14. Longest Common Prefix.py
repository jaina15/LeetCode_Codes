class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        mini=min(strs)
        maxi=max(strs)
        for i,c in enumerate(mini):
            if c!=maxi[i]:
                return mini[:i]
        return mini
