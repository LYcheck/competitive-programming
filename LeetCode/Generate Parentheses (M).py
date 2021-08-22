class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(op, cl, temp):
            if op == n and cl == n:
                res.append(str(temp))
                return
            if op < n:
                backtrack(op+1, cl, temp+'(')
            if op > cl:
                backtrack(op, cl+1, temp+')')

        res = []
        temp = ""
        backtrack(0, 0, temp)
        return res