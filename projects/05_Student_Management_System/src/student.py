class Student:
    def __init__(self, student_id, name, age, gender, score):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.gender = gender
        self.score = score

    def __str__(self):
        return(
            f"学号: {self.student_id}, "
            f"姓名: {self.name}, "
            f"年龄: {self.age}, "
            f"性别: {self.gender}, "
            f"成绩: {self.score}"
        )

