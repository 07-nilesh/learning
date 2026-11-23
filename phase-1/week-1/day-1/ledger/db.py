import sqlite3

def get_conn(path: str=":memory:")-> sqlite3.Connection:
    conn=sqlite3.connect(path)
    conn.commit()
    return conn
    

def init_db(conn:sqlite3.Connection)->None:
    cursor=conn.cursor()
    cursor.executescript("""CREATE TABLE IF NOT EXISTS accounts (
                            account_id    INTEGER PRIMARY KEY,
                            owner         TEXT NOT NULL,
                            city          TEXT NOT NULL,
                            balance_paise INTEGER,
                            opened_on     TEXT NOT NULL
                            );
                            CREATE TABLE IF NOT EXISTS transactions (
                            txn_id        INTEGER PRIMARY KEY,
                            account_id    INTEGER NOT NULL,
                            amount_paise  INTEGER NOT NULL,
                            kind          TEXT NOT NULL,
                            created_at    TEXT NOT NULL
                            );""")
    conn.commit()
    

def seed(conn:sqlite3.Connection)->None:
    cursor=conn.cursor()
    cursor.executescript("""INSERT INTO accounts VALUES
                        (1,'Asha Verma','Bhopal',1250000,'2024-01-15'),
                        (2,'Rohan Mehta','Indore',80000,'2024-03-02'),
                        (3,'Priya Sharma','Bhopal',4500000,'2023-11-20'),
                        (4,'Priya Sharma','Pune',15000,'2025-02-11'),
                        (5,'Imran Khan','Mumbai',NULL,'2025-06-30'),
                        (6,'Neha Iyer','Chennai',990000,'2024-09-09');
                        INSERT INTO transactions VALUES
                        (1,1,500000,'credit','2025-01-05'),
                        (2,1,-120000,'debit','2025-01-09'),
                        (3,2,80000,'credit','2025-01-10'),
                        (4,3,2500000,'credit','2025-01-12'),
                        (5,3,-750000,'debit','2025-01-20'),
                        (6,4,15000,'credit','2025-02-12'),
                        (7,6,990000,'credit','2025-02-14'),
                        (8,1,-30000,'debit','2025-02-15'),
                        (9,3,-200000,'debit','2025-02-18'),
                        (10,2,-5000,'debit','2025-02-20');""")
    conn.commit()

def accounts_by_city(conn:sqlite3.Connection,city: str)-> list[tuple]:
    cursor=conn.cursor()
    cursor.execute("select * from accounts where city=?",(city,))
    return cursor.fetchall()