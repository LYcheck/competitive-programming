class Solution:
    def countOrders(self, n: int) -> int:
        # a(n) = (2n)!/2^n
        # This is also the number of ways of arranging the elements of n distinct pairs, assuming the order of elements
        # is significant and the pairs are distinguishable. When the pairs are not distinguishable, see A001147 and 
        # A132101. For example, there are 6 ways of arranging 2 pairs [1,1], [2,2]: {[1122], [1212], [1221], [2211],
        # [2121], [2112]}. - Ross Drewe, Mar 16 2008
            
        return ((math.factorial(2*n))//(1 << n))%(10**9+7)
    