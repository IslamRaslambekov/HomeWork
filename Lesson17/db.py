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
        new_data = []
        for dat in data:
            new_data.append(list(dat))
        return new_data


def drop():
    with sq.connect('main.db') as con:
        cur = con.cursor()
        cur.execute("DROP TABLE data")
        cur.execute("""CREATE TABLE IF NOT EXISTS data (
                    link TEXT,
                    model TEXT,
                    price INTEGER,
                    old_price INTEGER)
                    """)


if __name__ == '__main__':
    show()
    # run_db('a', 'a', 1, 3)
    # print(show())
