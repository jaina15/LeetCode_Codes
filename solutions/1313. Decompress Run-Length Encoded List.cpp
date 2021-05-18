class Solution {
public:
    vector<int> decompressRLElist(vector<int>& num) {
        vector<int> v;
        for(int i=0;i<num.size();i+=2){
            if(i%2==0){
                int n=num[i];
                while(n>0){
                    v.push_back(num[i+1]);
                    n--;
                }
            }
        }
        return v;
    }
};
