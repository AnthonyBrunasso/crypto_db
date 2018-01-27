import db as db

import time

if __name__ == '__main__':
    d = db.connect_crypto_db()
    db.create_all_tables(d)
    db.fill_all_tables(d)

    minute = 0
    print('Press cntrl+C to to terminate this process.')
    while True:
        print('Tables will update in {0} minutes.'.format(str(60 - minute)))
        time.sleep(60)
        minute += 1
        if minute == 60:
            db.fill_all_tables(d)
            minute = 0
