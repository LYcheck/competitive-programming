class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        n1 = num1.split('+')
        n2 = num2.split('+')
        
        reRes = int(n1[0])*int(n2[0]) + -(int(n1[1].rstrip(n1[1][-1]))*int(n2[1].rstrip(n2[1][-1])))
        imRes = int(n1[1].rstrip(n1[1][-1]))*int(n2[0]) + int(n2[1].rstrip(n2[1][-1]))*int(n1[0])
        
        return str(reRes) + '+' + str(imRes) + 'i'
        
#         n1 = num1.split('+')
#         n2 = num2.split('+')
        
#         re1 = int(n1[0])
#         re2 = int(n2[0])
#         im1 = int(n1[1].rstrip(n1[1][-1]))
#         im2 = int(n2[1].rstrip(n2[1][-1]))
        
#         reRes = re1*re2 + -(im1*im2)
#         imRes = im1*re2 + im2*re1
        
#         res = str(reRes) + '+' + str(imRes) + 'i'
        
#         return res
    
        