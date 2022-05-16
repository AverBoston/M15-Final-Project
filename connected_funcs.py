# Author: E. Avery Boston
# Date: 05/15/22
# Summary: functions that are all linked to food ordering, taxes() for finding the cost with tax,
#          displayOptions() and descriptions() for printing out the options or showing what each item is,
#          sushi() calls all functions in order and runs the control loop for the selection process and
#          collects the data with its variables
# Variables:
#	taxRate: constant in the taxes(), local tax rate (float)
#       a: parameter placeholder in taxes() (num)
#       product: returned value from taxes() (float)
#       select: loop control variable for the sushi() selection (int)
#       BasicCost: constant in sushi(), price of basic rolls (float)
#       DeluxeCost: constant in sushi(), price of deluxe rolls (float)
#       itemCost[]: list of cost for item on a menu, product of either basicCost or deluxeCost and quantity (float)
#       orderCost: variable used to track the total cost of the order (float)
#       quantity[]: list of quantity of each item ordered (int)
#       orderItem[]: list of items ordered (str)
#       index: variable that is the positional index for the parallel lists (int)

# function that finds out the total with tax and returns that value as product
def taxes(a):
    taxRate = .07
    product = (taxRate * a) + a
    return product
# function showing sushi options and other options
def displayOptions():
    print("Pick a number to add the associated menu item to your order.")
    print("\nBasic Roll Options, $5.50 per a roll:")
    print("1. Salmon")
    print("2. Tuna")
    print("3. Eel")
    print("4. California")
    print("5. Fried Yam")
    print("\nDeluxe Roll Options, $9.50 per a roll:")
    print("6. Dragon")
    print("7. Hooiser")
    print("8. Hurricane")
    print("9. Cat's Favorite")
    print("\nType 10 for a brief description of each item")
    print("Type 11 to show order so far, 12 to show full menu again")
    print("Type 0 to stop picking menu items")
# function showing brief description of menu items
def descriptions():
    print("\nSalmon roll, raw salmon")
    print("Tuna roll, raw tuna")
    print("Eel roll, eel")
    print("California roll, imitation crab, avocado, and cucumber")
    print("Fried Yam roll, fried yam")
    print("\nDragon roll, eel and crab inside, topped with avocado and eel")
    print("Hooiser roll, pork, cream cheese, and avocado inside, bacon and bbq on top")
    print("Hurricane roll, shrimp, raw white tail, cream cheese inside, crab on top")
    print("Cat's Favorite roll, spicy raw tuna inside, topped with raw tuna slices")
# function that all ordering is dependent on, it calls on the other functions
# it gets the information from input for the orders so that it can be written to file
# or used for tax totals
def sushi():
    # Initialize variables
    
    select = '-1'      # loop option variable
    BasicCost = 5.50   # cost of a basic roll
    DeluxeCost = 9.50  # cost of a deluxe roll
    itemCost = []   # float list of cost for item on a menu, product of either basicCost or deluxeCost and quantity
    orderCost = 0   # float that holds the subtotal of the current order
    quantity = []   # integer list of number of each item
    orderItem = []  # string list of item names

    displayOptions()

    # while loop with a list of numbers that allows users to pick options
    # numbers 1 to 9 are mapped to a sushi menu item choice
    # number 10 is mapped to running descriptions, 11 is mapped to showing total so far, 12 is mapped to showing the menu again
    select = (input("\nEnter your choice or 0 to stop: "))
    index = 0
    while select != '0':
        if select == '1':
            quantity.append(int(input("How many would you like? ")))
            orderItem.append("Salmon roll    ")
            itemCost.append(quantity[index] * BasicCost)
            orderCost = orderCost + itemCost[index]
            index = index + 1
            
        elif select == '2':
            quantity.append(int(input("How many would you like? ")))
            orderItem.append("Tuna roll      ")
            itemCost.append(quantity[index] * BasicCost)
            orderCost = orderCost + itemCost[index]
            index = index + 1
            
        elif select == '3':
            quantity.append(int(input("How many would you like? ")))
            orderItem.append("Eel roll       ")
            itemCost.append(quantity[index] * BasicCost)
            orderCost = orderCost + itemCost[index]
            index = index + 1
            
        elif select == '4':
            quantity.append(int(input("How many would you like? ")))
            orderItem.append("California roll")
            itemCost.append(quantity[index] * BasicCost)
            orderCost = orderCost + itemCost[index]
            index = index + 1
            
        elif select == '5':
            quantity.append(int(input("How many would you like? ")))
            orderItem.append("Fried Yam roll ")
            itemCost.append(quantity[index] * BasicCost)
            orderCost = orderCost + itemCost[index]
            index = index + 1
            
        elif select == '6':
            quantity.append(int(input("How many would you like? ")))
            orderItem.append("Dragon roll    ")
            itemCost.append(quantity[index] * DeluxeCost)
            orderCost = orderCost + itemCost[index]
            index = index + 1
            
        elif select == '7':
            quantity.append(int(input("How many would you like? ")))
            orderItem.append("Hooiser roll   ")
            itemCost.append(quantity[index] * DeluxeCost)
            orderCost = orderCost + itemCost[index]
            index = index + 1

        elif select == '8':
            quantity.append(int(input("How many would you like? ")))
            orderItem.append("Hurricane roll ")
            itemCost.append(quantity[index] * DeluxeCost)
            orderCost = orderCost + itemCost[index]
            index = index + 1
            
        elif select == '9':
            quantity.append(int(input("How many would you like? ")))
            orderItem.append("Cat's Favorite roll")
            itemCost.append(quantity[index] * DeluxeCost)
            orderCost = orderCost + itemCost[index]
            index = index + 1

        elif select == '10':
            descriptions()

        elif select == '11':
            i = 0         
            print("Your order is: ")
            for x in range(0, index):
                print("  " + str(quantity[i]) + "  " + orderItem[i] + "  $" + str("{:.2f}".format(itemCost[i])))
                i = i + 1
            print("The subtotal is $" + str("{:.2f}".format(orderCost)))
        elif select == '12':
            displayOptions()
        # selection validation
        elif select != '0':
            print("Error... Please type a number between 1 and 12")
            
        select = (input("\nEnter a number 1 to 9 to pick an item, 10 for description,\n11 to show order so far, 12 to show full menu again \nor 0 to stop: "))
    # for loop shows final order with tax and subtotal
    # for loop control variable
    i = 0         
    print("Your final order is: ")
    for x in range(0, index):
        print("  " + str(quantity[i]) + "  " + orderItem[i] + "  $" + str("{:.2f}".format(itemCost[i])))
        i = i + 1
    print("The subtotal is $" + str("{:.2f}".format(orderCost)))

    result = taxes(orderCost)
    print("Cost with tax is: $" + str("{:.2f}".format((result))))
    # open order tracking file
    sushiReceipt_file = open('sushi_file.txt', 'a')
    # for loop control variable
    i = 0
    # Header for the record
    sushiReceipt_file.write("\n   ")
    sushiReceipt_file.write("\nQty  Item Name      Cost\n")
    # for loop for writing each parallel list element with its associated parallel list
    for x in range(0, index):
        sushiReceipt_file.write(str(quantity[i]) + "   ")
        sushiReceipt_file.write(orderItem[i] + "  ")
        sushiReceipt_file.write("$" + str("{:.2f}".format(itemCost[i])) + '\n')
        i = i + 1
    # subtotal and returned tax value are written to the end of the file
    sushiReceipt_file.write("The subtotal is:    $" + str("{:.2f}".format(orderCost))+ '\n')
    sushiReceipt_file.write("Cost with tax is:    $" + str("{:.2f}".format((result))) + '\n')
    # close order tracking file
    sushiReceipt_file.close()
    print("Order logged,\nPlease have your payment ready at the counter when you pick it up.")

