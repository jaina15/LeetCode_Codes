class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ''.join([i.lower() for i in s if i.isalnum()])
        return new_s == new_s[::-1]
