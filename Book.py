# Book class

import pandas as pd
class Book:
  def __init__(self):
    self.bookFile = 'Books.csv'
    self.readBookFile = pd.read_csv(self.bookFile)
#states price of book by ISBN
  def getPrice(self, ISBN):
    return self.readBookFile.loc[self.readBookFile['ISBN']== ISBN, 'Price'].iloc[0]

