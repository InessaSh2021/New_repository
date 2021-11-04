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
            return 'Ошибка оценка должна быть по 10-ти балльной системе'      
    
         
               
        
class Lecturer(Mentor):
   grades = {}
   courses_attached = []
   
  
    
class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'        
     
           
 
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