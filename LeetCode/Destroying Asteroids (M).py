class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        
        for _ in asteroids:
            if mass < _: return False
            mass += _
                
        return True