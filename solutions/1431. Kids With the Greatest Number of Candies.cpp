class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        vector<bool> v;
        int maxx=INT_MIN;
        for(int i=0;i<candies.size();i++){
            maxx=max(maxx,candies[i]);
        }
        for(int i=0;i<candies.size();i++){
            if(candies[i]+extraCandies>=maxx){
                v.push_back(true);
            }
            else v.push_back(false);
        }
        return v;
    }
};
