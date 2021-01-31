from coinbase.wallet.client import Client
import os

API_KEY = os.environ.get('API_KEY')
API_SECRET = os.environ.get('API_SECRET')
API_VERSION = '2020-04-18'
currency = 'EUR'

buy_price_threshold_min  = 10000
btcToBuyInEUR=5;

client = Client(API_KEY, API_SECRET, api_version=API_VERSION)

accounts = client.get_accounts()
primary_account = client.get_primary_account()
payment_methods = client.get_payment_methods()


def main():
  
    mymethod = method(payment_methods.data)
    payment_method = mymethod.id
    payment_wallet = mymethod.name

    print("Getting latest BTC price...");
    buy_price  = client.get_buy_price(currency=currency)
    print(f"Buy price BTC: {buy_price.amount} USD")
    btcToBuy=round(btcToBuyInEUR/float(buy_price.amount), 8);
    print("You want to buy " + str(btcToBuyInEUR) + buy_price.currency + " in BTC. Therefore you will buy " + str(btcToBuy) + " BTC")

    account = client.get_primary_account()
    if checkBalance(accounts):
        print("You have sufficient balance to buy")
        performBTCBuy(primary_account, payment_method, payment_wallet, buy_price, buy_price_threshold_min, btcToBuy )
    else:
        print("You have insufficient balance to buy")

def method(methods):
    for method in methods:
        if (method.name == "Euro-portemonnee"):
            payment_method = method.id
            print(payment_method)
            method = method

    return method

def checkBalance(accounts):
    for account in accounts.data:
        if (account.name == "EUR Wallet"):
            #print(account.balance.amount)
            print("Balance for account " + account.name + ": "+ str(account.balance) )
            if (btcToBuyInEUR <= float(account.balance.amount)):
                return True
            else:
                return False
   
def performBTCBuy(account, payment_method, payment_wallet, buy_price, buy_price_threshold_min, btcToBuy):
    print(f"About to buy {btcToBuy} BTC at price {buy_price.amount}{buy_price.currency} from {payment_wallet} and adding to {account.name}")
    #print(account)
    if float(buy_price.amount) <= buy_price_threshold_min:
        try:
            print("Executing the buy")
            buy = account.buy(
                    amount=btcToBuy,
                    currency="BTC",
                    payment_method=payment_method
            )
            print(buy)
            print("Purchase was successfull")
        except:
            print("Purchase was not successfull")
    
    else:
        print("Could not buy BTC as the curreny BTC price is above " + str(buy_price_threshold_min))            

if __name__ == "__main__": main()


