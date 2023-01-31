name = input("What's your name? ")

match name:

    case "Picard":
        print("The next Generation")
    case "Riker":
        print("The next Generation")
    case "Sisko":
        print ("Deep Space Nine")
    case "Janeway":
        print ("Voyager")
    case "Kirk":
        print("The Original Series")
    case "Archer":
        print("Enterprise")

    case _: 
        print("Who?")
