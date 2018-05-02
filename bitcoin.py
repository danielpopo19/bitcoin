import requests 
from decimal import Decimal
import unittest

class BitcoinValueServices():
  def getCurrentValueofBitcoin(self):
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    t = r.json()['bpi']['USD']['rate']
    t = t.replace(",","")   
    t = Decimal(t)
    t = float(t)
    return(t)
    

class BitcoinWallet():
  def __init__(self):
		  self.BTCBalance = 1
		  self.Address = '1F1tAaz5x1HUXrCNLbtMDqcw6o5GNn4xqX'

  def calculateUSD(self,balance):
    return(BitcoinValueServices.getCurrentValueofBitcoin(self)*balance)
    
def main():
  user = BitcoinWallet()
  print("Current BTC: " + str(user.BTCBalance) + '\n' + "USD amount is: " + str(user.calculateUSD(user.BTCBalance)) + '\n' + "From Wallet Address: "+user.Address)

    
class TestBitcoinWallet(unittest.TestCase):

  def test_BTCBalance(self):
    tempTest = BitcoinWallet()
    self.assertGreaterEqual(tempTest.BTCBalance,0) 
  
  def test_getCurrentValueofBitcoin(self):
    tempTest = BitcoinValueServices();
    self.assertGreaterEqual(BitcoinValueServices.getCurrentValueofBitcoin(self),0)
    
    
  def test_mockBitcoinValueServices(self):
    tempTest = BitcoinWallet()
    self.assertEqual(tempTest.BTCBalance*0,0)
    self.assertLessEqual(tempTest.BTCBalance*-1,0)
    self.assertGreaterEqual(tempTest.BTCBalance*1,0)
    self.assertNotEqual(tempTest.BTCBalance*'0',0)
    
  def test_fullTest(self):
    tempTest = BitcoinWallet();
    self.assertGreaterEqual(tempTest.calculateUSD(tempTest.BTCBalance),0)

  
if __name__ == '__main__':
  main()
  unittest.main()
  