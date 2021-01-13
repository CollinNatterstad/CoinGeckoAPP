import os
import psycopg2 as pg
from pycoingecko import CoinGeckoAPI

from dotenv import load_dotenv
load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_USER_PASS = os.getenv("DB_USER_PASS")
DB_PORT = os.getenv ("DB_PORT")

cg = CoinGeckoAPI()

CryptoPrice = cg.get_price(ids=['bitcoin, polkadot, ethereum'], vs_currencies= "usd", )

