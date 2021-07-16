class Solution {
    public int reverse(int x) {
        int ans = 0;
        int prev = 0;
        
        while(x != 0){
            int y = x % 10;
            x /= 10;
            
            ans = ans * 10 + y;
            
            if((ans-y) / 10 != prev) return 0;
            prev = ans;
        }
        return ans;
    }
}