#Grade boundary calc

def main():
    print("Welcome to grade calculation")
    moduleNumber = input ("Please enter the module number ") 
    gradecalc(moduleNumber)

def gradecalc(module):
    print("You have selected ", module)
    inputGrade = int(input("Please enter the grade of the module"))
    print("For ", module," the student has scored ", inputGrade)
    if(inputGrade >= 40):
        print("This grade is a pass ")
        
    if(inputGrade < 40):
        print("This grade is a fail")
    
    
main()
    
