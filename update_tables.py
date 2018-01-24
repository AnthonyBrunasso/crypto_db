import db as db

if __name__ == '__main__':
    d = db.connect_crypto_db()
    # Forces data to come in fresh
    db.remove_all_tables(d)
    db.create_all_tables(d)
    db.fill_all_tables(d)
