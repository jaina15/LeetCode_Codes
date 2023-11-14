class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        words = s.split()
        prev=-1
        for word in words:
            if word.isnumeric():
                if prev<int(word):
                    prev = int(word)
                else:
                    return False
        return True
