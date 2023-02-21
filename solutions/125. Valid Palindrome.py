class Solution:
    def isPalindrome(self, s: str) -> bool:
        str=''
        for i in s:
            if i.isalnum():
                str+=i.lower()
        return str==''.join(list(str)[::-1])
