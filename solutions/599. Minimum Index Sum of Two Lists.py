class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        d=dict()
        mini=1000000
        for i,v in enumerate(list1):
            d[v]=[0,i,0]
        
        for i,v in enumerate(list2):
            if v in d:
                d[v][0]=1
                d[v][2]=d[v][1]+i
                mini = min(mini,(d[v][1]+i))
        
        return [k for k,v in d.items() if v[0]==1 and v[2]==mini]
