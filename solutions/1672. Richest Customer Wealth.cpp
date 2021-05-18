class Solution {
public:
    int maximumWealth(vector<vector<int>>& a) {
        int ans=INT_MIN;
        for(int i=0;i<a.size();i++){
            int s=0;
            for(int j=0;j<a[i].size();j++){
                s+=a[i][j];
            }
            ans=max(ans,s);
        }
        return ans;
    }
};
