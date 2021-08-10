class Solution:
    def judgeCircle(self, moves: str) -> bool:
        origin=tuple((0,0))
        #print(origin)
        x,y=0,0
        for i in moves:
            if i=='U':
                y+=1
            elif i=='D':
                y-=1
            elif i=='L':
                x-=1
            elif i=='R':
                x+=1
        #print(x,y)
        position=tuple((x,y))
        #print(position)
        if origin==position:
            return True
        return False
