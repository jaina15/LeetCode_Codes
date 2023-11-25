class Solution:
    def countSeniors(self, details: List[str]) -> int:
        return len([c for c in details if int(c[11:13])>60])
