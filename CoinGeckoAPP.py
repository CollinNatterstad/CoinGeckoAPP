
def main():
    #importing libraries
    import os
    import psycopg2 as pg
    from psycopg2 import sql
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
    
  
    def connect_and_store():

        #shorting CoinGeckoAPI for easy access
        cg = CoinGeckoAPI()
        coins = ['bitcoin', 'ethereum','polkadot']

        #connects to coingecko through api, returns price for each coin.
        CryptoPrice = cg.get_price(ids= coins, vs_currencies= "usd")        

        #For loop that seperates data from json format and stored into variable. key,value allows us to seperate the pair and pass key directly into the asset variable.
        for key, value in CryptoPrice.items():
 
            #The core data we are collecting.
            #dictates which table data is directed towards.
            asset = str(key)
            call_value = value

            print(asset)
           
                        
            #price of asset takes both keys in cryptoprice json data and un-nests the price value. constructed as {keyone(asset):{keytwo(usd): pricevalue}}
            price = CryptoPrice[f'{key}']['usd']
            print(price)

            #posted date of time. 
            now = date.today()
            print(now)

            #opens connection to postgres database through psycopg2 
            conn = pg.connect(database = DB_NAME, user= DB_USER, password= DB_USER_PASS, host= DB_HOST, port= DB_PORT)
            
            #creating cursor to interact with database. 
            cur = conn.cursor()
            #confirming creation in terminal
            print("\ncreated cursor object:", cur)
            
            cur.execute(
                sql.SQL("insert into public.{} (date,price) values (%s, %s)")
                    .format(sql.Identifier(f'{asset}')),[now,price]) 
            print("Table Updated")

            #commits changes to database  
            conn.commit()

            #closes cursor
            cur.close()
            print("\nclosed cursor object:",cur)

            #closes connection to postgres database
            conn.close()        
    #function calls 
    connect_and_store()

if __name__ == "__main__":
    main()



    
    
         

