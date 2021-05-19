class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        //set<int> s;
        int n=1;
        sort(nums.begin(),nums.end());
        nums.erase( unique( nums.begin(), nums.end() ), nums.end() );
        for(int i=0;i<nums.size();i++){
            if(nums[i]>0){
                if(nums[i]!=n)
                    return n;
                n++;
            }
                
        }
        /*for(auto i:s){
            if(i!=n)
                return n;    
            n++;
        }*/
        return n;
    }
};
