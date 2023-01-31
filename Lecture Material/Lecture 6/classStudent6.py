class Student:
    def __init__(self, name, dept):
        if not name:
            raise ValueError("Invalid name")
        self.name = name
        self.dept = dept

    def __str__(self):
        return f"{self.name} from {self.dept}"

    # Getter for dept
    @property
    def dept(self):
        return self._dept

    # Setter for dept
    @dept.setter
    def dept(self, dept):
        if dept not in ["CEMS", "NATS", "HSS"]:
            raise ValueError("Invalid Dept")
        self._house = dept


def main():
    student = get_student()
    print(student)


def get_student():
    name = input("Name: ")
    dept = input("Dept: ")
    return Student(name, dept)


if __name__ == "__main__":
    main()