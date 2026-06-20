import sqlite3


conn=sqlite3.connect(
"passwords.db"
)


cursor=conn.cursor()



cursor.execute("""
CREATE TABLE IF NOT EXISTS passwords(
website TEXT,
password TEXT
)
""")


conn.commit()


def add(site,password):

    cursor.execute(
    "INSERT INTO passwords VALUES(?,?)",
    (site,password)
    )

    conn.commit()



def show():

    cursor.execute(
    "SELECT * FROM passwords"
    )

    return cursor.fetchall()
