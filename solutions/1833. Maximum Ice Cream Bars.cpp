class Solution {
public:
    int maxIceCream(vector<int>& cost, int coins) {
        sort(cost.begin(),cost.end());
        int c=0;
        for(int i=0;i<cost.size();i++){
            if(coins-cost[i]<0){
                break;
            }
            else{
                coins-=cost[i];
                c++;
            }
        }
        return c;
    }
};
