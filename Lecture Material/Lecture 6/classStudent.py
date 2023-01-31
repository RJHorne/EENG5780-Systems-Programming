class Student:
    ...

def main():
    student = get_student()
    print(f"{student.name} from {student.dept}")


def get_student():
    student = Student()
    student.name = input("Name: ")
    student.dept = input("Dept: ")
    return student


if __name__ == "__main__":
    main()