class Student:
    def __init__(self, name, dept):
        if not name:
            raise ValueError("Missing name")
        if dept not in ["CEMS", "NATS", "HSS"]:
            raise ValueError("Invalid dept")
        self.name = name
        self.dept = dept

    def __str__(self):
        return f"{self.name} from {self.dept}"



def main():
    student = get_student()
    print(student)


def get_student():
    name = input("Name: ")
    dept = input("Dept: ")
    student = Student(name, dept)
    return student
    # return Student(name,dept)


if __name__ == "__main__":
    main()