class Solution {
public:
    int numIdenticalPairs(vector<int>& num) {
        int c=0;
        int a[101]={0};
        for(int i=0;i<num.size();i++){
            a[num[i]]++;
        }
        for(int i=0;i<101;i++){
            if(a[i]>0){
                c+=(((a[i]*(a[i]-1)))/2);
            }
        }
        return c;
    }
};
