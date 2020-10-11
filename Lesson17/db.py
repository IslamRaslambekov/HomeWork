import sqlite3 as sq


def run_db(n_link, n_model, n_price, n_old_price):
    with sq.connect('main.db') as con:
        cur = con.cursor()
        # cur.execute("DROP TABLE data")
        cur.execute("""CREATE TABLE IF NOT EXISTS data (
            link TEXT,
            model TEXT,
            price INTEGER,
            old_price INTEGER)
            """)
        cur.execute("INSERT INTO data VALUES (?,?,?,?)", (n_link, n_model, n_price, n_old_price))


def show():
    with sq.connect('main.db') as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM data")
        data = cur.fetchall()
        for dat in data:
            print(list(dat))


if __name__ == '__main__':
    # run_db('a', 'a', 1, 3)
    show()
