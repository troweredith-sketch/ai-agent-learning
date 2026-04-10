class StudentManager:
    def __init__(self):
        self.students = []

    def find_student_by_id(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None
    
    def add_student(self, student):
        if self.find_student_by_id(student.student_id) is not None:
            return False
        self.students.append(student)
        return True
    
    def remove_student(self, student_id):
        student = self.find_student_by_id(student_id)
        if student is None:
            return False
        self.students.remove(student)
        return True
    
    def update_student(self, student_id, name=None, age=None, gender=None, score=None):
        student = self.find_student_by_id(student_id)
        if student is None:
            return False

        if name is not None:
            student.name = name
        if age is not None:
            student.age = age
        if gender is not None:
            student.gender = gender
        if score is not None:
            student.score = score

        return True
    
    def get_all_students(self):
        return self.students
    
