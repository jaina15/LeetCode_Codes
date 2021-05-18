class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        set<int> s;
        int i=0;
        for(i=0;i<nums.size();i++){
            if(s.find(nums[i])!=s.end()){
                return nums[i];
            }
            s.insert(nums[i]);
        }
        return -1;
    }
};
