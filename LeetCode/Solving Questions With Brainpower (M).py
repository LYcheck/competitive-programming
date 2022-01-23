class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        maxpoints = [0 for q in questions]
        maxsofar = 0
    
        for _ in range(n):
            points = questions[_][0]
            brainpower = questions[_][1]
            nexti = _+brainpower+1
            
            maxsofar = max(maxsofar, maxpoints[_] + points)
            
            if nexti < n:
                maxpoints[nexti] = max(maxpoints[nexti], maxpoints[_] + points)
            if _ < n-1:
                maxpoints[_+1] = max(maxpoints[_], maxpoints[_+1])
            
        return maxsofar