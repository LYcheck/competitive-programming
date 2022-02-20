class Solution(object):
    def depthSum(self, nestedList):
        def recurse(nestedList, depth):
            res = 0
            
            for element in nestedList:
                if element.isInteger():
                    res += element.getInteger() * depth
                else:
                    res += recurse(element.getList(), depth+1)
                    
            return res
        
        return recurse(nestedList, 1)