class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        n = len(sandwiches)
        cnt_0 = 0
        for i in range(n):
            if students[i] == 0:
                cnt_0 += 1
        cnt_1 = n - cnt_0
        for i in range(n):
            if sandwiches[i] == 0 and cnt_0 > 0:
                cnt_0 -= 1
            elif sandwiches[i] == 1 and cnt_1 > 0:
                cnt_1 -= 1
            else:
                return n - i
        return 0