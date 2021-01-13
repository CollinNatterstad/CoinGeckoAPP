import os
import psycopg2 as pg
from pycoingecko import CoinGeckoAPI

from dotenv import load_dotenv
load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_USER_PASS = os.getenv("DB_USER_PASS")
DB_PORT = os.getenv ("DB_PORT")

cg = CoinGeckoAPI()
ids = ["Bitcoin","Polkadot","Ethereum"]

CryptoPrice = cg.get_price(ids= ids, vs_currencies= "usd", )
print(CryptoPrice)

class databaseconnection:
    try: 
        conn = pg.connect(database = DB_NAME, user = DB_USER, password = DB_USER_PASS, host = DB_HOST, port = DB_PORT )
        print ("Database Connection Successful")
    
    except:
        print ("Database Connection Unsuccessful")