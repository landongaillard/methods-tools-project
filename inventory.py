# Inventory class

import numpy as np
import pandas as pd
from Book import Book

class Inventory:
  def __init__(self):
    self.inventoryFile = 'InventoryList.csv'
    self.inventoryList = pd.read_csv(self.inventoryFile)

  ## adds quantity of items back to inventory, this function gets called in Cart class
  ## when item is deleted from Cart
  def addBackQuantity(self, ISBN, quantity):
    self.inventoryList.loc[self.inventoryList['ISBN'] == ISBN, 'Quantity'] += int(quantity)
    self.inventoryList.to_csv(self.inventoryFile, encoding='utf-8', index=False)

  
  def delInventory(self,ISBN,quantity):
    self.inventoryList.loc[self.inventoryList.ISBN == ISBN, "Quantity"] -= int(quantity)
    self.inventoryList.to_csv(self.inventoryFile, encoding='utf-8', index=False)
  def printInventory(self):
    book = Book()
    inventory_list = book.readBookFile.merge(self.inventoryList, on='ISBN')
    print(inventory_list)
    print("######## Inventory List ########\n")
    print(inventory_list)

  def checkItemQuantity(self, ISBN, quantity):
      isbn_filtered = self.inventoryList[self.inventoryList['ISBN'] == ISBN]
      
      if not isbn_filtered.empty:
          # Convert the 'Quantity' column to integer
          isbn_filtered = isbn_filtered.copy()
          isbn_filtered.loc[:, 'Quantity'] = isbn_filtered['Quantity'].astype(int)
          
          if isbn_filtered.at[isbn_filtered.index[0], 'Quantity'] >= int(quantity):
              return True
          else:
              return False
      else:
          return False
