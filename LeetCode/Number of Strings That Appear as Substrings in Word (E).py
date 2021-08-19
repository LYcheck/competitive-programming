class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        cnt = 0
        for _ in patterns:
            if _ in word:
                cnt += 1
        return cnt