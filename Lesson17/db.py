import sqlite3 as sq


def run_db(link, model, price, old_price):
    with sq.connect('main.db') as con:
        cur = con.cursor()
        # cur.execute("DROP TABLE data")
        cur.execute("""CREATE TABLE IF NOT EXISTS data (
            link TEXT,
            model TEXT,
            price INTEGER,
            old_price INTEGER)
            """)
        cur.execute("INSERT INTO data VALUES (?,?,?,?)", (link, model, price, old_price))


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


def pro_task_table(surname, name, middle_name, number, email, password):
    with sq.connect('pro.db') as con:
        cur = con.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS proData (
                            surname TEXT,
                            name TEXT,
                            middle_name TEXT,
                            number TEXT,
                            email TEXT,
                            password TEXT)
                            """)
        cur.execute("INSERT INTO proData VALUES (?,?,?,?,?,?)", (surname, name, middle_name, number, email, password))


def pro_task_show():
    with sq.connect('pro.db') as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM proData")
        data = cur.fetchall()
        new_data = []
        for dat in data:
            new_data.append(list(dat))
        return new_data


if __name__ == '__main__':
    show()
    # run_db('a', 'a', 1, 3)
    # print(show())
