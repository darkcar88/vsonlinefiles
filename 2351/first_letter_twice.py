class Solution:
    def repeatedCharacter(self, s: str) -> str:
        count = defaultdict(int)
        
        for ch in s:
            if count[ch] + 1 == 2:
                return ch
            else:
                count[ch] += 1

        return ''