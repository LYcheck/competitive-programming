class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [0]*(len(s)+1)
        dp[0] = 1
        
        for i in range(1, len(s)+1):
            for w in wordDict:
                if dp[i-len(w)] and s[i-len(w):i] == w:
                    dp[i] = 1
                    
        print(dp)
                    
        return dp[len(s)]