class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        pangram = list('thequickbrownfoxjumpsoverthelazydog')
        for c in pangram:
            if c not in sentence:
                return False
        return True
