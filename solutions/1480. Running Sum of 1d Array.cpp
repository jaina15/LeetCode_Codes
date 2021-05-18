class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        vector<int> sum;
        int t=0;
        for(int i=0;i<nums.size();i++){
            sum.push_back(t+nums[i]);
            t=t+nums[i];
        }
        return sum;
    }
};
