import MySQLdb

def connect_crypto_db():
    db = MySQLdb.connect(host="localhost",
        user="root",
        passwd="root",
        db="cryptics")

    return db

def create_all_tables(db):
    create_currency_change_table(db)

def create_currency_change_table(db): 
    cur = db.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS currency_change(\
       name varchar(255),\
       four_hour decimal(6,2),\
       one_day decimal(6,2),\
       seven_day decimal(6,2),\
       two_weeks decimal(6,2),\
       one_month decimal(6,2))")

