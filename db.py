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
            open decimal(22,10),\
            high decimal(22,10),\
            low decimal(22,10),\
            close decimal(22,10),\
            volume decimal(22,10),\
            time varchar(120),\
            base_value decimal(22,10))".format(market))

def fill_all_tables(db):
    cur = db.cursor()
    markets = bittrex.get_all_market_summaries()
    num = 0
    for market in markets:
        ticks = bittrex.get_ticks(market)
        market = market.replace('-', '_')
        num += 1
        print("Updating table {0} {1}/{2}".format(market, num, len(markets)))
        for t in ticks:
            qry = "INSERT INTO {0} VALUES ({1},\
                {2},\
                {3},\
                {4},\
                {5},\
                '{6}',\
                {7})".format(
                market,
                str(t.base_volume),
                str(t.close_value),
                str(t.high_value),
                str(t.low_value),
                str(t.open_value),
                str(t.timestamp),
                str(t.volume))
            cur.execute(qry)
            db.commit()
