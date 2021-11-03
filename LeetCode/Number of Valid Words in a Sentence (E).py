class Solution:
    def countValidWords(self, sentence: str) -> int:
        words = sentence.split(' ')
        marks = {'!', ',', '.'}
        res = 0
        
        for word in words:
            if word == '':
                continue
                
            hypok = 1
            punctok = 1
            alpha = 1
            
            n = len(word)
            
            punct = word.count('.') + word.count(',') + word.count('!')
            hyp = word.count('-')
            
            if punct > 1:
                punctok = 0
            elif punct == 1:
                if word[n-1] not in marks:
                    punctok = 0

            if hyp > 1:
                hypok = 0
            elif hyp == 1:
                if word[n-1] == '-' or word[0] == '-':
                    hypok = 0
                else:
                    idx = word.index('-')
                    if not (word[idx-1].isalpha() and word[idx+1].isalpha()):
                        hypok = 0
            
            for _ in word:
                if (_.isalpha() and ord(_)-97 < 26) or _ in marks or _ == '-':
                    continue
                else:
                    alpha = 0
                        
            if alpha and punctok and hypok:
                #print(word)
                res += 1
                
        return res
 
                    
                    
                    