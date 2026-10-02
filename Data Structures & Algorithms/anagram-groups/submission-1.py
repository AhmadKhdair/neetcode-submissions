class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for word in strs:
            arr=[0]*26
            for char in word:
                arr[ord(char)-ord("a")]+=1
            key=tuple(arr)
            if key in d.keys():
                d[key].append(word)
            else:
                d[key]=[word]
        finalList=[]
        for key in d:
            finalList.append(d[key])
        return finalList