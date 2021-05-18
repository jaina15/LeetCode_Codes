class Solution {
public:
    vector<int> shuffle(vector<int>& num, int n) {
        vector<int> v;
        for(int i=0;i<n;i++){
            v.push_back(num[i]);
            v.push_back(num[i+n]);
        }
        return v;
    }
};
