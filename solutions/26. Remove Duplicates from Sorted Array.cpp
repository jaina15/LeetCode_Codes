class Solution {
public:
    int removeDuplicates(vector<int>& a) {
        int j=0;
        if(a.size()==0 || a.size()==1)
            return a.size();
        for(int i=0;i<a.size()-1;i++){
            if(a[i]!=a[i+1])
                a[j++]=a[i];
        }
        a[j++]=a[a.size()-1];
        return j;
    }
};
