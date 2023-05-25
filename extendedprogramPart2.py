#A program that gives the user a choice of using an calculator app or to read from a text file
import os

#functions for calculations
def calculate(num1, num2, operator_choice):
    if operator_choice == "1":
        print(num1, "+", num2, "=", (num1 + num2), file=f)
        return num1 + num2
        

    elif operator_choice == "2":
        print(num1, "-", num2, "=", (num1 - num2), file=f)
        return num1 - num2

    elif operator_choice == "3":
        print(num1, "*", num2, "=", (num1 * num2), file=f)
        return num1 * num2

    elif operator_choice == "4":
        if num2 == 0:
            raise ValueError ("Invalid input, cannont divide by 0")
                                                
        else:
            print(num1, "/", num2, "=", (num1 / num2), file=f)
            return num1 / num2

    else:
        raise ValueError ("You have entered an invalid entry, please try again")
        
while True:
    choice = input("Please choose if you'll like to (a) 'Use the calculator application' or (b) 'Read equations from a text file: \n")
    if choice.lower() == "a":
                #defining the operators
                print("Operator choices")
                print("1 Addition")
                print("2 Subtraction")
                print("3 Multiplication")
                print("4 Division")
    
                #Output equations to be written to text file
                with open ("output.txt", "a") as f:

                    while True:
                        try:
                            operator_choice = input("Please select from the above operators: ")
                            num1 = int(input("Please enter number 1: "))
                            num2 = int(input("Please enter number 2: "))
                            sum = calculate(num1, num2, operator_choice)
                            print(sum)
                            more_calculations = input("Would you like to do more calculations? (yes/no):")
                            if more_calculations.lower() == "no":
                                break
                    
                        except ValueError:
                                print("Invalid input, please try again")
                    break
    elif choice.lower() == "b":
         while True:
              try:
                  filename = input("Please enter the filename: ")
                  myfile = open(filename)
                  equatations = myfile.readlines()
                  print(equatations)
                  myfile.close()
                  break
              except FileNotFoundError:
                   print("The file you entered cannot be found.")
         break

    else:
         print("You've entered an invalid choice, please try again")