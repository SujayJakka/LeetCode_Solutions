class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mapThing = {"A" : 0, "B":0, "C" : 0, "D":0, "E" : 0, "F":0, "G" : 0, "H":0, "I" : 0, "J":0, "K" : 0, "L":0, "M" : 0, "N":0, "O" : 0, "P":0, "Q" : 0, "R":0, "S" : 0, "T": 0, "U" : 0, "V": 0, "W" : 0, "X": 0, "Y" : 0, "Z": 0,}

        res = 0

        l = 0
        for i in range(len(s)):
            mapThing[s[i]] += 1

            maxValue = max(mapThing.values())

            if((i - l + 1) - maxValue <= k):
                res = i - l + 1
            else:
                mapThing[s[l]] -= 1
                l += 1
        
        return res
