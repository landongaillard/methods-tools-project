# Cart class
import string
import random
import pandas as pd
from Inventory import Inventory
from Book import Book
class Cart:
  def __init__(self,username):
    self.userName = username
    self.ISBN = None
    self.quantity = None
    self.orderFile = 'orders.csv'
    self.orderList = pd.read_csv(self.orderFile)
    self.cartItemList = pd.DataFrame(columns=['ISBN', 'Quantity', 'Price/item'], dtype=object)

  def AddToCart(self,item,quantity):
    self.ISBN = item
    self.quantity = quantity
    book = Book()
    price = book.getPrice(item)
    new_row = pd.Series({"ISBN": item, "Quantity": quantity, "Price/item": price})
    self.cartItemList = pd.concat([self.cartItemList, new_row.to_frame().T], axis=0, ignore_index=True)

  def removeFromCart(self, ISBN):
    self.cartItemList.drop(self.cartItemList[self.cartItemList['ISBN'] == ISBN].index, inplace=True)

  ## check if the entered ISBN is in the cart so to delete or not
  ## returns quantity or False (0)
  def checkCart(self, ISBN):
    for i in range(len(self.cartItemList.index)):
      if (self.cartItemList.loc[i]['ISBN'] == ISBN):
          return self.cartItemList.loc[i]['Quantity']
    
    return 0

  #adds item from cart back to inventory
  
  def addBackToInventory(self, inventory):
    for i in range(len(self.cartItemList.index)):
      isbn = self.cartItemList.loc[i]['ISBN']
      quantity = int(self.cartItemList.loc[i]['Quantity'])
      inventory.addBackQuantity(isbn, quantity)

  
  def checkout(self,inventory,customer):
    if self.checkItems():
      print("Cannot checkout Empty Cart")
      return
    
    totalPrice = 0
    for i in range(len(self.cartItemList.index)):
      # ISBN = self.cartItemList.loc[i].ISBN
      quantity = int(self.cartItemList.loc[i]['Quantity'])
      price = int(self.cartItemList.loc[i]['Price/item'].replace('$', ''))
      total = quantity * price
      totalPrice = totalPrice + total  ## total price of cart items
      print(f"Total cost of the books selected: ${totalPrice}")
    #Card Sequence and billing
    while True:
      cardNum = input("Enter your Card Number: ")
      if cardNum.isnumeric() == True:
        break
      else:
        print("Invalid entry. Please enter Numeric value only.")
    
    cardName = input("Name on Card: ")
    billAddr = input("Enter your Billing Address Street Number and Name: ")
    billCity = input("Enter the city: ")
    billState = input("Enter the State: ")
    billZip = input("Enter the ZipCode: ")
    orderID = ''.join(random.choices(string.ascii_uppercase +  string.digits, k = 4)) # random string with numbers of length 4

    for i in range(len(self.cartItemList.index)):
      ISBN = self.cartItemList.loc[i].ISBN
      quantity = int(self.cartItemList.loc[i].Quantity)
      price = int(self.cartItemList.loc[i]['Price/item'].replace('$', ''))
      total = quantity * price
      self.addOrder(cardName,cardNum,billAddr,billCity,billState,billZip,ISBN,quantity,price,total,orderID)

    recordCardInfo = input("Save this card for future? \n  Yes(y) No(N) \n")

    if recordCardInfo.lower() == 'y':
      customer.setPaymentInfo(cardName,cardNum,billAddr,billCity,billState,billZip)
    
    #self.goodList = pd.DataFrame(columns=['ISBN', 'Quantity'], dtype=object)
    self.orderList.to_csv(self.orderFile, encoding='utf-8', index=False)

  def addOrder(self,cardName,cardNum,billAddr,billCity,billState,billZip,ISBN,quantity,price,total,orderID):
    new_row = pd.Series({"userName":self.userName,"cardName":cardName,"cardNum":cardNum,"billAddr":billAddr,
              "billCity":billCity,"billState":billState,"billZip":billZip,"ISBN":ISBN,"quantity":quantity,"price":price,
              "total":total,"orderID":orderID})
    self.orderList = pd.concat([self.orderList, new_row], ignore_index=True)

  def removeOrder(self,username):
    self.orderList = self.orderList.drop(self.orderList.index[self.orderList['user'] == username])
    self.orderList.to_csv(self.orderFile, encoding='utf-8', index=False)

  def checkItems(self):
    if (len(self.cartItemList.index)==0):
      return True
    return False

  def printCart(self):
    if len(self.cartItemList) > 0:
      print("********** CART LIST **********")
      print(self.cartItemList)
      print("*******************************")
    else:
      print("\n******** CART IS EMPTY ********")
