import java.util.Stack;

class Solution {
    public boolean isValid(String s) {
        Stack order = new Stack();
        
        if(s.length() == 0) return true;
        if(s.length() == 1) return false;

        for(int i = 0; i < s.length(); i++){
            char cur = s.charAt(i);
            
            if(cur == ')' || cur == ']' || cur == '}') {
                if(order.empty()) return false;
                else if(cur == ')' && (char)order.peek() == '(') order.pop();
                else if(cur == ']' && (char)order.peek() == '[') order.pop();
                else if(cur == '}' && (char)order.peek() == '{') order.pop();
                else return false;
                }

            else order.push(cur);
            }
        return order.empty();
    }
}