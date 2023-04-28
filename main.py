# main file
# interface to access the account 
# menu options
from Customer import Customer
from Inventory import Inventory
from Cart import Cart


   
from os import system ,name
def clear():
    if name == 'nt':
        _ = system('cls ')

    else: 
        _ = system('clear')


# verifying the user account

print("--------  VALHALA BOOKSTORE  ------- \n")
print("------------ GROUP_16 -------------\n")
while True:
    print("1. LogIn \n2. Create Account \n3. Exit Program\n ")
    selectMenu = input("Select an option. ")
    
    
    if selectMenu == '1':
        userName = input("UserName : ")
        password = input("Password : ")
        customer = Customer(userName)
        if customer.isUser()== True and customer.checkPassword(userName,password) == True:
            fName = customer.customersInfo.loc[customer.customersInfo['username'] == customer.userName, 'fname'].iloc[0]
            lName = customer.customersInfo.loc[customer.customersInfo['username'] == customer.userName, 'lname'].iloc[0]
            print(f"\n----- Welcome! {fName.upper()} {lName.upper()} --------")
            break
        else:
            print("\nWrong UserName or Password, Try Again!\n")
    elif selectMenu == '2':
        print("\nCreating an Account\n")
        userName = input("UserName : ")
        password = input("Password : ")
        conf_password = input("Confirm Password : ")
        customer = Customer(userName)

        for i in range(2):    ## confirm password offers for 3 times
            if password != conf_password:
                print("Password did not match. Try Again!")
                conf_password = input("Confirm Password:")
          
        if password != conf_password: ## if not confirmed yet, start over
            print("Couldn't Match Password. Try Again!\n")
            continue
        
        else:  ## adds user to the customer csv file
            customer.addUser(userName,password)
            #verify = True ########
            print("\n------------- Creating Account -------------\n")
            firstname = input("Enter your First Name: ")
            lastname = input("Enter your Last Name: ")
            customer.setName(firstname,lastname)
            
            print(" Account Successfully Created.")
            print(" Welcome ", firstname.upper(), lastname.upper())
            shipAddr = input("Enter Street Number and Name : ")
            shipCity = input("Enter the City : ")
            shipState = input("Enter the State : ")
            shipZip = input ("Enter the Zip: ")
            customer.setShippingAddress(shipAddr,shipCity,shipState,shipZip)
            break

    elif selectMenu == '3':
        exit()
    
    else:
        print("Please select valid option.")


if True:
    #### create inventory object ####
    inventory = Inventory()
    #### create Cart object ####
    cart = Cart(userName)
    inventory.printInventory()

    while True:
        print("\nSelect Options Below")
        options = input("\n(A) Account Info \n(I) Inventory Info \n(C) Cart Info \n(L) Log Out\n")

        if options.lower() == 'a':
            print("\n************* Account Information **************")
            editAccount = True
            while editAccount:
                print("\nACCOUNT OPTIONS:")
                accMenu = input("(A) View Account Information \n(U) Update Account Information\n(P) Edit Payment Information\n(D) Delete Account\n(B) Return Back\n")
                
                viewAccount = True
                while viewAccount:
                    if accMenu.lower() == 'a':
                        customer.printAccountDetails()
                        viewAccount = False
                    
                    elif accMenu.lower() == 'u':
                        accSubMenu = input ("(N) Update Name \n(S) Edit Shipping Address\n(B) Account Menu\n")
                        if accSubMenu.lower() == 'n':
                            firstname = input("Update First Name: ")
                            lastname = input("Update Last Name: ")
                            customer.setName(firstname, lastname)
                            print("Account Updated Sucessfully.\n")  
                            viewAccount = False
                        elif accSubMenu.lower() == 's':
                            shipAddr = input("Enter Street Number and Name : ")
                            shipCity = input("Enter the City : ")
                            shipState = input("Enter the State : ")
                            shipZip = input ("Enter the Zip: ")
                            customer.setShippingAddress(shipAddr,shipCity,shipState,shipZip)
                            viewAccount = False
                        elif accSubMenu.lower() == 'b':
                            viewAccount = False
                        
                    elif accMenu.lower() == 'p':
                        print("\nUpdating Payment Information")
                        while True:
                            cardNum = input("Enter Card Number: ")
                            if cardNum.isnumeric() == True:
                                break
                            else:
                                print("Invalid entry. Please enter Numeric value only.")
    
                        cardName = input("Name on Card: ")
                        billAddr = input("Enter your Billing Address Street Number and Name: ")
                        billCity = input("Enter the city: ")
                        billState = input("Enter the State: ")
                        billZip = input("Enter the ZipCode: ")
                        customer.setPaymentInfo(cardName, cardNum, billAddr, billCity, billState, billZip)
                        viewAccount = False

                    elif accMenu.lower() == 'd':
                        customer.deleteAccount(cart)
                        viewAccount = False

                    elif accMenu.lower() == 'b':
                        viewAccount = False

                    else:
                        print("Enter valid entry\n")
                        viewAccount = False
                
                if accMenu.lower() == 'b':
                    editAccount = False
        
        # prints inventory 
        elif options.lower() == 'i':
            inventory.printInventory()
        
        ## cart information selection
        elif options.lower() == 'c':
            Cart = customer.getCart()
            editCart = True
            while editCart:
                Cart.printCart()
                cartOption = input("\n1. Add to Cart\n2. View Cart\n3. View Inventory\n4. Delete Cart Item\n5. Checkout\n6. Return Back\n")
                if cartOption.lower() == '1':
                    ISBN = input("\nEnter ISBN number :")
                    quantity = input("\nItem Quantity :")

                    if inventory.checkItemQuantity(ISBN, quantity):
                        Cart.AddToCart(ISBN, quantity)
                        inventory.delInventory(ISBN, quantity) ## reduce the quantity from inventory
                    else:
                        continue

                elif cartOption.lower() == '2':
                    Cart.printCart()

                elif cartOption.lower() == '3':
                    inventory.printInventory()

                elif cartOption.lower() == '4':
                    ISBN = input("\nEnter ISBN number to remove: ")
                    quantity = Cart.checkCart(ISBN) ### might check if already empty, cart.print
                    inventory.addBackQuantity(ISBN,quantity) ### addQuantity
                    Cart.removeFromCart(ISBN)

                elif cartOption.lower() == '5':
                    Cart.checkout(inventory,customer)
                    editCart = True

                elif cartOption.lower() == '6':
                    editCart = False
                
                

        elif options.lower() == 'l':
            Cart = customer.getCart()
            checkItems = Cart.checkItems()
            if checkItems:
                Cart.addBackToInventory(inventory)
            customer.logout()
