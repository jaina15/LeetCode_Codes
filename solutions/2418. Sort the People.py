class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        li = [(names[i],heights[i]) for i in range(len(names))]
        li.sort(key = lambda x:x[1],reverse=True)
        return [li[i][0] for i in range(len(li))]
