def solution(s):
    # Your code here
    # Create lookup table -> O(n)?
    # If capital, preppend capchar -> 000001
    
    ans = ""
                
    codes = ["100000", "110000", 
            "100100", "100110", 
            "100010", "110100", 
            "110110", "110010", 
            "010100", "010110",
            "101000", "111000",
            "101100", "101110",
            "101010", "111100",
            "111110", "111010",
            "011100", "011110",
            "101001", "111001",
            "010111", "101101",
            "101111", "101011"
            ]
    
    for char in s:
        ascii = ord(char)
        
        if ascii == 32:
            ans += "000000"
            
        elif ascii < 97:
            ans += "000001"
            char = char.lower()
            print(char)
            ans += codes[ord(char)-97]
            
        else:
            ans += codes[ord(char)-97]
    
    return ans

print(solution("Bruh"))
