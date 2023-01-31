def main():
    student = get_student()
    print(f"{student['name']} from {student['dept']}")


def get_student():
    student = {}
    student["name"] = input("Name: ")
    student["dept"] = input("Dept: ")
    return student
    #return {"name": name, "house": house}

if __name__ == "__main__":
    main()