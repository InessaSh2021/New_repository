class Mentor:
    def __init__(self, name, surname, courses_attached):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    def rate_lect(self, student, mentor, course, grade):
        if isinstance(student, Student) and course in mentor.courses_attached and course in student.courses_in_progress:
            if course in student.grades and 0 < grade < 11:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'ќшибка оценка должна быть по 10-ти балльной системе'
        
    def __lt__(self, Lecturer):
        if not isinstance(self, Lecturer):
            print("Not a Lecturer")
            return
        return self.get_sum_lecturer_grades < other.get_sum_students_grades        
                           
        
class Lecturer(Mentor):
   grades = {}
   courses_attached = []
   
   def get_sum_lecturer_grades(Lecturer):
       sum_lecturer_grades = 0
       for courses_attached in self.lecturer_grades:
           sum_lecturer_grades += sum(Lecturer['grades'])/len(Lecturer['grades'])
       return round(sum_lecturer_grades, 2)
      
   def __str__(self):
       res = f'Ћектор {self.name}_{self.surname}. —редн€€ оценка за лекции{get_sum_lecturer_grades(Lecturer)}'
       return  res
   print(Lecturer)
    
    
class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'ќшибка'
         
    def get_sum_students_grade(students, course):
        sum_students_grade = 0
        for student in students:
            sum_students_grade += sum(student['grade'])/len(students['grade'])
            return round(students_sum_grade/len(students), 2)
        print(get_sum_students_grade, 2) 
        
      
           
 
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

megan_fox = Lecturer('Megan', 'Fox', 'Python')
  
cool_mentor = Mentor('Some', 'Buddy', 'Python')
#cool_mentor.courses_attached += ['Python']
cool_reviewer = Reviewer('vasia', 'pupkin', 'Python')
#cool_reviewer.courses_attached += ['Python']
print() 
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
best_student.rate_lect(best_student, megan_fox, 'Python', 5)
 
print(best_student.name, best_student.grades)

print(cool_reviewer.name, cool_reviewer.surname, cool_reviewer.courses_attached)
print(cool_mentor.name, cool_mentor.surname, cool_mentor.courses_attached)
print(megan_fox.name, megan_fox.surname, megan_fox.courses_attached, megan_fox.grades)