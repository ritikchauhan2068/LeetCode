class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
        total=0
        prev=0

        for i in reversed(s):
            v=roman_map[i]
            if v < prev:
                total-=v
            else:
                total+=v
            prev=v
        return total
        
        