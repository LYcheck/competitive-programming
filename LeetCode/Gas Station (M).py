class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if not gas: return -1
        
        tank, total, res = 0, 0, 0
        
        for i in range(len(gas)):
            tank += gas[i]-cost[i]
            if tank < 0:
                res = i+1
                tank = 0
            
            total += gas[i] - cost[i]
            
        return res if total >= 0 else -1