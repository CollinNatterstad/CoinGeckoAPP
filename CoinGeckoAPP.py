
def main():
    #importing libraries
    import os, json
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
    def connect_API():
        #shorting CoinGeckoAPI for easy access
        cg = CoinGeckoAPI()
        coins = ['Bitcoin', 'Ethereum','Polkadot']
        #connects to coingecko through api, returns price for each coin.
        CryptoPrice = cg.get_price(ids= coins, vs_currencies= "usd")

        now = date.today()

        for key,value in CryptoPrice.items():
            


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

    #function calls 
    connect_API()  



if __name__ == "__main__":
    main()



    
    
         

