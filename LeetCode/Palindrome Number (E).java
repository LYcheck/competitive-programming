class Solution {
    public boolean isPalindrome(int x) {
        int temp = x;
        int result = 0;
        
        while(x > -1){
            int pres = temp % 10;
            temp /= 10;
            
            result = result * 10 + pres;
            
            if(temp == 0 && result != x) return false;
            if(temp == 0 && result == x) return true;
        }
        return false;
    }
}