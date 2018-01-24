import MySQLdb
import urllib.request, json
import bittrex as bittrex

def connect_crypto_db():
    db = MySQLdb.connect(host="localhost",
        user="root",
        passwd="root",
        db="cryptics")

    return db

def create_all_tables(db):
    create_currency_tables(db)

def remove_all_tables(db):
    cur = db.cursor()
    markets = bittrex.get_all_market_summaries()
    for market in markets:
        cur.execute("DROP TABLE IF EXISTS {0}".format(market.replace('-', '_')))

def create_currency_tables(db): 
    cur = db.cursor()
    markets = bittrex.get_all_market_summaries()
    for market in markets:
        cur.execute("CREATE TABLE IF NOT EXISTS {0}(\
            bid decimal(20,8))".format(market.replace('-', '_')))

def test(db):
    cur = db.cursor()
    cur.execute("INSERT INTO {0} VALUES ({1})".format(
        "USDT-ZEC".replace('-', '_'),
        str(4.7)))
    db.commit() 

def fill_all_tables(db):
    cur = db.cursor()
    markets = bittrex.get_all_market_summaries()
    for market in markets:
        prices = bittrex.get_market_history(market)
        print("Updating table {0}".format(market))
        for price in prices:
            cur.execute("INSERT INTO {0} VALUES ({1})".format(
                market.replace('-', '_'),
                str(price))) 
            db.commit()
