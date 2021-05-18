class Solution {
public:
    int largestAltitude(vector<int>& gain) {
        vector<int> v;
        int ans=INT_MIN,s=0;
        v.push_back(s);
        for(int i=0;i<gain.size();i++){
            s+=gain[i];
            //v.push_back(s);
            ans=max(ans,s);
        }
        //sort(v.rbegin(),v.rend());
        //ans=v[0];
        if(ans<0)
            return 0;
        return ans;
    }
};
