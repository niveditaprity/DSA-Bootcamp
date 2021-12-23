class Solution:
    def compress(self, chars: List[str]) -> int:
        count = 1
        j = 0
        for i in range(1, len(chars)):
            if(chars[i-1]==chars[i]):
                count+=1
            elif(chars[i-1]!=chars[i]):
                chars[j] = chars[i-1]
                j+=1
                if(count>1):
                    for k in str(count):
                        chars[j] = k
                        j+=1
                        count = 1
                    
        chars[j] = chars[-1]
        j+=1
        if(count>1):
            for k in str(count):
                chars[j] = k
                j+=1
                    
        return j