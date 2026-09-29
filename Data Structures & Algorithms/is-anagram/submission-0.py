class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arrS=[0] * 26
        arrT=[0] * 26
        for x in s:
            index=ord(x)-ord('a')
            arrS[index]+=1
        for y in t:
            index=ord(y)-ord('a')
            arrT[index]+=1
        return arrS==arrT
