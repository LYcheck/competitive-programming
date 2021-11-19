class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        pos = [0, 0]
        face = [0, 1]
        
        
        for ins in instructions:
            if ins == 'G':
                pos[0] += face[0]
                pos[1] += face[1]
                
            elif ins == 'L':
                face[0], face[1] = -face[1], face[0]
            
            else:
                face[0], face[1] = face[1], -face[0]
                
        return pos == [0, 0] or face != [0,1]