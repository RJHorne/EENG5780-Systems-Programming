def main():
    name, dept = get_student()
    print(f"{name} from {dept}")


def get_student():
    name = input("Name: ")
    dept = input("Dept: ")
    return name, dept


if __name__ == "__main__":
    main()