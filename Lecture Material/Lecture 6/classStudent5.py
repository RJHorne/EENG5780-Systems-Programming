class Student:
    def __init__(self, name, dept, proj=None):
        if not name:
            raise ValueError("Missing name")
        if dept not in ["CEMS", "NATS", "HSS"]:
            raise ValueError("Invalid dept")
        self.name = name
        self.dept = dept
        self.proj = proj

    def __str__(self):
       return f"{self.name} from {self.dept}"
   
    def special(self):
        match self.proj:
            case "robot":
                return "🕹" 
            case "pill":
                return "💊"
            case _:
                return "💩"



def main():
    student = get_student()
    print(student.special())


def get_student():
    name = input("Name: ")
    dept = input("Dept: ")
    proj = input("Project: ")
    return Student(name,dept,proj)


if __name__ == "__main__":
    main()