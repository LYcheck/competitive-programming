class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stk = []
        while pushed or popped:
            if not popped: break
                
            target = popped[0]
            if stk and stk[-1] == target:
                popped.pop(0)
                stk.pop(-1)
            else:
                if not pushed: break
                stk += [pushed[0]]
                pushed.pop(0)
                
        return len(popped) == 0