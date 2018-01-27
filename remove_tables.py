import db as db

if __name__ == '__main__':
    d = db.connect_crypto_db()
    db.remove_all_tables(d)
