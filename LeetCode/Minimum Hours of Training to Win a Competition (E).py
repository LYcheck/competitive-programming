class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        ene, exp = initialEnergy, initialExperience
        eneeded, expneeded = 0, 0
        
        for i in range(len(energy)):
            if ene > energy[i]: pass
            else: 
                eneeded += energy[i]+1-ene
                ene = energy[i]+1
    
            if exp > experience[i]: pass
            else:
                expneeded += experience[i]+1-exp
                exp = experience[i]+1
            
            exp += experience[i]
            ene -= energy[i]
            
        return expneeded + eneeded