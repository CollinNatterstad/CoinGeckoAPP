#importing libraries
import os
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

cg = CoinGeckoAPI()

#returns prices for these coins. 
ids = ["Bitcoin","Polkadot","Ethereum"]

#connects to coingecko through api, returns price for each coin.
CryptoPrice = cg.get_price(ids= ids, vs_currencies= "usd")

#connects to local database. 
class databaseconnection:
    
    conn = pg.connect(database = DB_NAME, user = DB_USER, password = DB_USER_PASS, host = DB_HOST, port = DB_PORT )
    
    conn.close()
    
    
         

