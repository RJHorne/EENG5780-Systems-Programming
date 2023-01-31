def main():
    student = get_student()
    if student[0] == "Robert":
        student[1] = "CEMS"
    print(f"{student[0]} from {student[1]}")


def get_student():
    name = input("Name: ")
    dept = input("Dept: ")
    return (name, dept)


if __name__ == "__main__":
    main()