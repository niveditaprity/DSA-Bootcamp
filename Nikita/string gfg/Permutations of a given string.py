from itertools import permutations
class Solution:
    def find_permutation(self, S):
        l=[]
        for i in permutations(S,len(S)):
            l.append(''.join(i))
        l.sort()
        return l
