#importing libraries
import os
import json
import psycopg2 as pg
from pycoingecko import CoinGeckoAPI

#importing dotenv for access to .env file
from dotenv import load_dotenv
load_dotenv()

#connecting .env contents to a program variable
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_USER_PASS = os.getenv("DB_USER_PASS")
DB_PORT = os.getenv ("DB_PORT")

#function containing api call. 
def connect_API():
    #shorting CoinGeckoAPI for easy access
    cg = CoinGeckoAPI()
    #list of interested coins. 
    cryptolist = ["Bitcoin","Polkadot","Ethereum"]

    #for loop iterates over each coin and brings back pricing data. this data will then be manipulated and pushed to databases.     
    for coin in cryptolist:
        #connects to coingecko through api, returns price for each coin.
        CryptoPrice = cg.get_price(ids= coin, vs_currencies= "usd")
        print(CryptoPrice)        


def update_tables():
    conn = pg.connect(database = DB_NAME, user= DB_USER, password= DB_USER_PASS, host= DB_HOST, port= DB_PORT)

    conn.close()

#Operations involving local database. 
connect_API()
update_tables()






    
    
         

