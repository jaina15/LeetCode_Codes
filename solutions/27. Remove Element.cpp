class Solution {
public:
    int removeElement(vector<int>& a, int val) {
        int j=0;
        for(int i=0;i<a.size();i++){
            if(a[i]!=val){
                a[j++]=a[i];
            }
        }
        //a[j++]=a[a.size()-1];
        return j;
    }
};
