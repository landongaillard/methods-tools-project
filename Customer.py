# Customer class file

import pandas as pd
from Cart import Cart

class Customer:
  def __init__(self,userName):
    self.userName = userName
    self.password = None 
    self.firstName = None
    self.lastName = None
    self.cardName = None
    self.cardNumber = None
    self.billingAddress = None
    self.billingCity = None
    self.billingState = None
    self.billingZip = None
    self.shippingAddress = None
    self.shippingCity = None
    self.shippingState = None
    self.shippingZip = None
    self.cart = Cart(userName)  ## Cart object as customer attribute in constructor
    self.readFile = 'customer.csv'
    self.customersInfo = pd.read_csv(self.readFile) ## read customer.csv file


# setting name and storing it in customer file
  def setName(self,firstName,lastName):
    self.firstName = firstName
    self.lastName = lastName
    self.customersInfo.loc[self.customersInfo['username'] == self.userName,'fname'] = firstName
    self.customersInfo.loc[self.customersInfo['username'] == self.userName,'lname'] = lastName 
    self.customersInfo.to_csv(self.readFile, index = False)
#Sets PaymentInfo and stores it in file
  def setPaymentInfo(self, cardName, cardNumber, billingAddr, billingCity, billingState, billingZip):
    self.cardName = cardName
    self.cardNumber = cardNumber
    self.billingAddress = billingAddr
    self.billingCity = billingCity
    self.billingState = billingState
    self.billingZIP = billingZip
    self.customersInfo.loc[self.customersInfo['username'] == self.userName, 'cardName'] = cardName
    self.customersInfo.loc[self.customersInfo['username'] == self.userName, 'cardNum'] = cardNumber
    self.customersInfo.loc[self.customersInfo['username'] == self.userName, 'billingAddr'] = billingAddr
    self.customersInfo.loc[self.customersInfo['username'] == self.userName, 'billCity'] = billingCity
    self.customersInfo.loc[self.customersInfo['username'] == self.userName, 'billState'] = billingState
    self.customersInfo.loc[self.customersInfo['username'] == self.userName, 'billZip'] = billingZip
    self.customersInfo.to_csv(self.readFile, index = False)
    print(self.customersInfo.loc[self.customersInfo['username'] == self.userName]) 
    # prints the row (user account informations) with userName == userName


  def setShippingAddress(self, shippingAddr,shippingCity,shippingState,shippingZip):
    self.shippingAddress = shippingAddr
    self.shippingCity = shippingCity
    self.shippingState = shippingState
    self.shippingZip = shippingZip
    self.customersInfo.loc[self.customersInfo['username'] == self.userName, 'shipAddr'] = shippingAddr
    self.customersInfo.loc[self.customersInfo['username'] == self.userName, 'shipCity'] = shippingCity
    self.customersInfo.loc[self.customersInfo['username'] == self.userName, 'shipState'] = shippingState
    self.customersInfo.loc[self.customersInfo['username'] == self.userName, 'shipZip'] = shippingZip
    self.customersInfo.to_csv(self.readFile, index = False)
    print("Shipping Adress successfully set\n")
    print(self.customersInfo.loc[self.customersInfo['username'] == self.userName])
    # prints the row (user account informations) with userName == userName

 
  ## returns items (books) in the cart
  def getCart(self):
    return self.cart
  
  ## adding user to the csv file (customer.csv)
  def addUser(self, username,password):
    new_row = pd.Series({'username': username, 'password': password})
    self.customersInfo = pd.concat([self.customersInfo, new_row.to_frame().T], axis=0, ignore_index=True)
    self.customersInfo.to_csv(self.readFile, index=False)

  ## verify if username is in the file
  def isUser(self):
    if self.userName in self.customersInfo['username'].unique():
      return True
    return False

  ## verify if password for username in the file is correct
  def checkPassword(self,username,password):
    uname = self.customersInfo.loc[self.customersInfo['username'] == self.userName,'username'].iloc[0]
    pwd = self.customersInfo.loc[self.customersInfo['username'] == self.userName,'password'].iloc[0]
    if uname == username and pwd == password:
      return True
    else:
      return False
  
  ## delete account of user with cart items 
  def deleteAccount(self,cart):
    self.customersInfo = self.customersInfo.drop(self.customersInfo[self.customersInfo['username']==self.userName].index)
    self.customersInfo.to_csv(self.readFile, index = False)
    print('Account is Deleted\n')
    exit()
  
  ## print account detais
  def printAccountDetails(self):
    df = (self.customersInfo.loc[self.customersInfo.index[self.customersInfo['username'] == self.userName]])
    print(df[['username','password','fname','lname','cardName','cardNum','billAddr','billCity','billState','billZip','shipAddr','shipCity','shipState','shipZip']])

  ## logout 
  def logout(self):
    exit()
