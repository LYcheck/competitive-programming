class Solution {
public:
    int countNumbersWithUniqueDigits(int n) {
        //credit to amanmehara, didn't properly reason combin
        if(n == 0) return 1;
        
        int ans = 10;
        int base = 9;
        
        for(int i = 9, j = 1; i > 0 && j < n; i--, j++ ){
            base *= i;
            ans += base;
        }
        
        return ans;
    }
};
