class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk = []
        
        for ast in asteroids:
            if not stk or ast > 0: 
                stk += [ast]
            else:
                while stk and stk[-1] > 0 and stk[-1] < abs(ast):
                    stk.pop()
                    
                if not stk or stk[-1] < 0:
                    stk += [ast]
                elif stk[-1] > 0 and stk[-1] == -ast:
                    stk.pop()
                
        return stk