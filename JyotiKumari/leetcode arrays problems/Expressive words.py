class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        count = 0
        for word in words:
            i,j,n,m = 0,0,len(s),len(word)
            flag = 1
            for i in range(n):
                if j<m and s[i] == word[j]:
                    j+=1
                elif s[i-1:i+2] != s[i]*3 != s[i-2:i+1]:
                    flag = 0
                    break
            if(flag and j==m):
                count+=1
        return count