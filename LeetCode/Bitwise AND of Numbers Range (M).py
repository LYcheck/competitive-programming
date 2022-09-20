class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # HAHAHAHHAHAHAHAHAHHAHA CHIPSELECT QUESTION THANKS 224
        if left^right == 0: return left&right
        pos = int(math.log2(left^right))
        return (left&right)&~((1<<(pos+1))-1) 