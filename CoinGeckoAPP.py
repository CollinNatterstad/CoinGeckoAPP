
def main():
    #importing libraries
    import os
    import json
    import psycopg2 as pg
    from psycopg2.extras import json
    from pycoingecko import CoinGeckoAPI
    from datetime import date

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
    def connect_bitcoin():
        #shorting CoinGeckoAPI for easy access
        cg = CoinGeckoAPI()
    
        #connects to coingecko through api, returns price for each coin.
        CryptoPrice = cg.get_price(ids= 'bitcoin', vs_currencies= "usd")

        now = date.today()

        #opens connection to postgres database through psycopg2 
        conn = pg.connect(database = DB_NAME, user= DB_USER, password= DB_USER_PASS, host= DB_HOST, port= DB_PORT)
        #creating cursor to interact with database. 
        curr = conn.cursor()
        print("\ncreated cursor object:", curr)

        #curr.execute("Insert INTO Bitcoin")



        #commits changes to database
        conn.commit()
        #closes cursor
        curr.close()
        #closes connection to postgres database
        conn.close() 
            
    def connect_ethereum():

        cg = CoinGeckoAPI()
        CryptoPrice = cg.get_price(ids= 'ethereum', vs_currencies= "usd")
        print(CryptoPrice)
        conn = pg.connect(database = DB_NAME, user= DB_USER, password= DB_USER_PASS, host= DB_HOST, port= DB_PORT)

        conn.close() 
    def connect_polkadot():

        cg = CoinGeckoAPI()
        CryptoPrice = cg.get_price(ids= "polkadot", vs_currencies= "usd")
        print(CryptoPrice)
        conn = pg.connect(database = DB_NAME, user= DB_USER, password= DB_USER_PASS, host= DB_HOST, port= DB_PORT)

        conn.close() 


  

    #function calls 
    connect_bitcoin()
    connect_ethereum()
    connect_polkadot()
    



if __name__ == "__main__":
    main()



    
    
         

