def main():
    student = get_student()
    if student["name"] == "Robert":
        student["dept"] = "CEMS"
    print(f"{student['name']} from {student['dept']}")


def get_student():
    name = input("Name: ")
    dept = input("Dept: ")
    return {"name": name, "dept": dept}


if __name__ == "__main__":
    main()