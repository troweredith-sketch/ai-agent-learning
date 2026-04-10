from student import Student
from student_manager import StudentManager

def show_menu():
    print("\n===== 学生管理系统 =====")
    print("1. 添加学生")
    print("2. 查看所有学生")
    print("3. 查找学生")
    print("4. 修改学生")
    print("5. 删除学生")
    print("0. 退出系统")

def input_student_info():
    student_id = input("请输入学号：").strip()
    if not student_id:
        print("学号不能为空！")
        return None

    name = input("请输入姓名：").strip()
    if not name:
        print("姓名不能为空！")
        return None

    while True:
        age_input = input("请输入年龄：").strip()
        try:
            age = int(age_input)
            break
        except ValueError:
            print("年龄输入格式不正确，请重新输入！")

    while True:
        score_input = input("请输入成绩：").strip()
        try:
            score = float(score_input)
            break
        except ValueError:
            print("成绩输入格式不正确，请重新输入！")

    gender = input("请输入性别：").strip()

    return student_id, name, age, gender, score

def handle_add_student(manager):
    print("\n--- 添加学生 ---")
    info = input_student_info()
    if info is None:
        return

    student_id, name, age, gender, score = info
    student = Student(student_id, name, age, gender, score)

    if manager.add_student(student):
        print("添加学生成功！")
    else:
        print("添加失败：学号已存在。")

def handle_show_all_students(manager):
    print("\n--- 所有学生信息 ---")
    students = manager.get_all_students()

    if not students:
        print("当前没有学生信息。")
        return

    for student in students:
        print(student)

def handle_find_student(manager):
    print("\n--- 查找学生 ---")
    student_id = input("请输入要查找的学号: ").strip()
    student = manager.find_student_by_id(student_id)

    if student is None:
        print("未找到该学生。")
    else:
        print("查找结果：")
        print(student)

def handle_remove_student(manager):
    print("\n--- 删除学生 ---")
    student_id = input("请输入要删除的学号: ").strip()

    if manager.remove_student(student_id):
        print("删除成功！")
    else:
        print("删除失败：未找到该学生。")

def handle_update_student(manager):
    print("\n--- 修改学生 ---")
    student_id = input("请输入要修改的学号: ").strip()
    student = manager.find_student_by_id(student_id)

    if student is None:
        print("未找到该学生。")
        return

    print("当前学生信息：")
    print(student)
    print("直接回车表示不修改该项。")

    name = input("请输入新姓名: ").strip()
    age_input = input("请输入新年龄: ").strip()
    gender = input("请输入新性别: ").strip()
    score_input = input("请输入新成绩: ").strip()

    name = name if name else None
    gender = gender if gender else None

    age = None
    if age_input:
        try:
            age = int(age_input)
        except ValueError:
            print("年龄输入格式不正确，修改失败！")
            return

    score = None
    if score_input:
        try:
            score = float(score_input)
        except ValueError:
            print("成绩输入格式不正确，修改失败！")
            return

    if manager.update_student(student_id, name=name, age=age, gender=gender, score=score):
        print("修改成功！")
    else:
        print("修改失败！")

def main():
    manager = StudentManager()

    while True:
        show_menu()
        choice = input("请选择操作: ").strip()

        if choice == "1":
            handle_add_student(manager)
        elif choice == "2":
            handle_show_all_students(manager)
        elif choice == "3":
            handle_find_student(manager)
        elif choice == "4":
            handle_update_student(manager)
        elif choice == "5":
            handle_remove_student(manager)
        elif choice == "0":
            print("感谢使用学生管理系统，再见！")
            break
        else:
            print("无效选项，请重新输入。")


if __name__ == "__main__":
    main()