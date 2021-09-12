class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        cur, add, candidate = 0, 0, 0
        
        # reset = minutes
        
        for minute in range(len(customers)):
            if not grumpy[minute]:
                cur += customers[minute]
            else:
                candidate += customers[minute]
                
            if minute > minutes and grumpy[minute-minutes]:
                candidate -= customers[minute-minutes]
            
            add = max(add, candidate)
        
        return cur + add