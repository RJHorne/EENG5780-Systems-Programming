def main():
    name = get_name()
    dept = get_dept()
    print(f"{name} from {dept}")

def get_name():
    return input("Name: ")

def get_dept():
    return input("Dept: ")

if __name__ == "__main__":
    main()
