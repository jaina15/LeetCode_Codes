#level/depth of a node in an ordered binary tree can be calculated using this depth=int(math.log(node)/math.log(2))
#minimum value in a level or at a depth can be calculated using 2**(depth)
#maximum value in a level or at a depth can be calculated using 2**(depth+1)-1
#offset is calculated to know how much we have to add to the minimum to reach the correct ordered node
#offset=maxi-label
#to reach correct ordered node-> add offset to the minimum value of the level. mini+offset
class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        l=[]
        l.append(label)
        while label!=1:
            depth=int(math.log(label)/math.log(2))
            #print('depth',depth)
            mini=2**depth
            #print('mini',mini)
            maxi=2**(depth+1)-1
            #print('maxi',maxi)
            offset=maxi-label
            #print('offset',offset)
            label=int((mini+offset)/2)
            #print('label',label)
            l.append(label)
        
        #print(l)
        return l[::-1]
