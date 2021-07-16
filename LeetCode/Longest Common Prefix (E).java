class Solution {
    public String longestCommonPrefix(String[] strs) {
        if(strs.length == 0){ return ""; }
        if (strs.length == 1) { return strs[0]; }
        
        String pre = strs[0];
        
        for(String word : strs){
            int count = 0;
            for(int i = 0; i <= word.length(); i++){
                try{ 
                    if(word.charAt(i) == pre.charAt(i)){ count++; }
                    else{ pre = pre.substring(0, count); }
                    }
                catch(Exception e){ pre = pre.substring(0, count); }
            }
        }
        return pre;
    }
}