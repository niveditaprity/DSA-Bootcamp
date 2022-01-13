class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        final1 = []
        final2 = []
        for element in s:
            if element!='#':
                final1.append(element)
            elif element == '#' and len(final1)>0:
                final1.pop()

        for element in t:
            if element!='#':
                final2.append(element)
            elif element == '#' and len(final2)>0:
                final2.pop()
        if final1 == final2:
            return True
        
