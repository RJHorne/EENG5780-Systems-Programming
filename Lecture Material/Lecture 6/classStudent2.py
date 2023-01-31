class Student:
    def __init__(self, name, dept):
        self.name = name
        self.dept = dept


def main():
    student = get_student()
    print(f"{student.name} from {student.dept}")


def get_student():
    name = input("Name: ")
    dept = input("Dept: ")
    # student = Student(name, dept)
    # return student
    return Student(name,dept)


if __name__ == "__main__":
    main()