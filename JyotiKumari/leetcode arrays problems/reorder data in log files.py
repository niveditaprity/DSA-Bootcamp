class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters = []
        nums = []
        for log in logs:
            if (log.split()[1]).isalpha():
                letters.append(log.split())
            else:
                nums.append(log)
        letters.sort(key = lambda x : x[0])
        letters.sort(key = lambda x : x[1:])
        for i in range(len(letters)):
            letters[i] = (" ".join(letters[i]))
        letters.extend(nums)
        
        return letters