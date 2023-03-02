class Solution:
    def average(self, salary: List[int]) -> float:
        mini=10000000
        maxi=-1
        total=0
        for i in salary:
            mini=min(mini,i)
            maxi=max(maxi,i)
            total+=i
        total=total-mini-maxi
        return total/(len(salary)-2)
