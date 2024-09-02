class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        changing = True
        counter = len(students)
        while changing:
            changing = False
            temp = []
            n = len(students)
            i = 0
            while i < n:
                if students[0] == sandwiches[0]:
                    sandwiches.pop(0)
                    counter -= 1
                    students.pop(0)
                    changing = True
                else:
                    temp.append(students.pop(0))
                i += 1
            students = temp
        return counter
                    
