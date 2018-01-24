import db as db

if __name__ == '__main__':
    d = db.connect_crypto_db()
    db.create_all_tables(d)
