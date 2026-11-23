from ledger.db import get_conn,init_db,seed,accounts_by_city
import sqlite3
import pytest
def test_init_is_idempotent():
    conn=get_conn()
    init_db(conn)
    init_db(conn)
    cursor=conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name IN ('accounts', 'transactions')")
    rows=cursor.fetchall()
    assert len(rows)==2


def test_duplicate_pk_rejected():
    conn=get_conn()
    init_db(conn)
    seed(conn)
    cursor=conn.cursor()
    with pytest.raises(sqlite3.IntegrityError):
        cursor.execute("INSERT INTO accounts VALUES (1,'Test','X',0,'2025-01-01'); ")

def test_accounts_by_city():
    conn=get_conn()
    init_db(conn)
    seed(conn)
    assert len(accounts_by_city(conn, "Bhopal")) == 2
    assert len(accounts_by_city(conn, "Nowhere")) == 0
