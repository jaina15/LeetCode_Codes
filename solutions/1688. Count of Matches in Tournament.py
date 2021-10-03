class Solution:
    def numberOfMatches(self, n: int) -> int:
        return n-1
        #no_of_team_advances=0
        #no_of_matches=0
        #total_match=0
        #if n==1:
        #    return 0
        #while no_of_team_advances!=1:
        #    if n%2==0:
        #        no_of_team_advances=n//2
        #        no_of_matches=n//2
        #        n=no_of_team_advances
        #    else:
        #        no_of_team_advances=(n-1)//2
        #        no_of_matches=((n-1)//2)+1
        #        n=no_of_team_advances
        #    total_match+=no_of_matches
        #return total_match
