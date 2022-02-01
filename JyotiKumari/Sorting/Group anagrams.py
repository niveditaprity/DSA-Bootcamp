class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = []
        lookup = {}
        for string in strs: 
            key = "".join(sorted(string))
            if key in lookup: 
                lookup[key].append(string)
            else: 
                lookup[key] = [string]
        for anagram in lookup: 
            anagrams.append(lookup[anagram])
        
        return anagrams