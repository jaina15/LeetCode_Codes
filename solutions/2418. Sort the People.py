class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return [i[0] for i in sorted(zip(names,heights),key=lambda x:x[1],reverse=True)]
