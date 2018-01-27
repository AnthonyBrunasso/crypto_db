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
        market = market.replace('-', '_')
        print('Deleting table {0}'.format(market))
        cur.execute("DROP TABLE IF EXISTS {0}".format(market))

def create_currency_tables(db): 
    cur = db.cursor()
    markets = bittrex.get_all_market_summaries()
    for market in markets:
        market = market.replace('-', '_')
        print('Creating table {0}'.format(market))
        cur.execute("CREATE TABLE IF NOT EXISTS {0}(\
            bid decimal(20,8))".format(market))

def fill_all_tables(db):
    cur = db.cursor()
    markets = bittrex.get_all_market_summaries()
    for market in markets:
        prices = bittrex.get_market_history(market)
        market = market.replace('-', '_')
        print("Updating table {0}".format(market))
        for price in prices:
            cur.execute("INSERT INTO {0} VALUES ({1})".format(
                market,
                str(price))) 
            db.commit()
