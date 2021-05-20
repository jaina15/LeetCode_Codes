class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        for(int i=0;i<nums2.size();i++){
            nums1.push_back(nums2[i]);
        }
        sort(nums1.begin(),nums1.end());
        int s=nums1.size();
        if(s<1)
            return nums1[0];
        else{
            if(s%2==0){
                int medb=(s/2)-0.5;
                int meda=(s/2)+0.5;
                cout<<nums1[medb]<<"  "<<nums1[meda];
                return double(nums1[medb]+nums1[meda])/2;
            }
            else{
                int med=s/2;
                return nums1[med];
            }
        }
    }
};
