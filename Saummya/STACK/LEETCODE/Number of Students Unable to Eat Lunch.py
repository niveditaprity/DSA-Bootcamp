class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count_ = 0
        while(count_ <= len(sandwiches)):
            if students[0]==sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                count_=0
                
            if len(students)==0:
                return 0
            
            else:
                temp=students[0]
                students=students[1:]
                students.append(temp)
                count_+=1
                
        return len(students)
