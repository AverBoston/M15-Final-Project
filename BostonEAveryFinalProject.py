# Program name: The Bento Box Ordering System
# Author: E. Avery Boston
# Date: 05/3/22
# Summary: main module for the program, opens the program, calls on primary functions, and exits from the program
# Variables:
#	choice: loop control variable (int)


# import the functions
import connected_funcs
import review_func

# main function that starts and ends the program and calls on the functions in other files
def main():
    # Initialize loop option variable
    choice = '-1'

    # Loop to show and run intial menu options
    # Welcome message and multiple number option menu
    print("\nWelcome to The Bento Box Ordering System!")
    print("Select a number to pick an option.")
    print("1  To place an order")
    print("2  To leave a review")
    print("3  To leave the program")
    while choice != '3':
        choice = (input("Enter your choice(1 to order, 2 to review, 3 to leave): "))
        print()
        # if and elif statements to allow selection control
        if choice == '1':
            connected_funcs.sushi()
        elif choice == '2':
            review_func.feedback()
        # selection validation
        elif choice != '3':
            print("Error... Please choose a number from 1 to 3.\n1 to place an order, 2 to leave a review, \nor 3 to leave program")
        
    # Exit message
    print("Thank you for using The Bento Box!")

main()
          
