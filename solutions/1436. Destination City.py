class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        seen_dep = {}
        for path in paths:
            seen_dep[path[0]]=1
        for path in paths:
            if path[1] not in seen_dep:
                return path[1]
        return
