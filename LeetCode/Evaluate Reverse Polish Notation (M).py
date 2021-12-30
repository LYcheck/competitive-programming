class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        ops = []
        opset = {'+':0, '-':0, '/':0, '*':0}
        
        for char in tokens:
            if char not in opset:
                nums.append(int(char))
            else:
                op2 = nums.pop()
                op1 = nums.pop()
                
                if char == '+':
                    nums.append(op1+op2)
                elif char == '-':
                    nums.append(op1-op2)
                elif char == '/':
                    div = op1/op2
                    div = ceil(div) if div < 0 else floor(div)
                    nums.append(div)
                elif char == '*':
                    nums.append(op1*op2)
        
        return nums[0]