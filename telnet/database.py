#!/bin/python

import sqlite3
from hashlib import sha256

def create_connection(db_file):
    conn = sqlite3.connect(db_file)
    conn.row_factory = sqlite3.Row
    return conn

def create_challenge_table(conn):
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS challenge (
        ID INTEGER PRIMARY KEY,
	    RFID TEXT,
        START_TS real NOT NULL,
        RESULT_TS real,
        USER TEXT NOT NULL,
        PASS TEXT NOT NULL,
        LEVEL INTEGER,
        WG_PASS TEXT,
        TOKEN TEXT,
        IPADR TEXT,
        NICKNAME TEXT
    )
    ''')
    conn.commit()

def insert_user(conn, rfid):
    cur = conn.cursor()
    cur.execute('INSERT INTO challenge(RFID, USER, PASS, LEVEL, START_TS) VALUES (?, ?, ?, ?, ?)', (rfid, get_user(rfid), get_pass(rfid), 1, time.time()))
    conn.commit()

def fetch_user(conn, rfid):
    cur = conn.cursor()
    cur.execute('SELECT * FROM challenge WHERE RFID=?', (rfid,))
    return cur.fetchone()

def get_user(rfid):
    hash_string = sha256(rfid.encode()).hexdigest()
    user = 'u0x' + hash_string.lower()[:8]
    return user

def get_pass(rfid):
    bytes_array = bytes.fromhex(rfid)
    hash_bytes = sha256(bytes_array).hexdigest().upper()[:8]
    return hash_bytes

conn = create_connection('foo.db')
create_challenge_table(conn)

user = ',,,,7;)'
insert_user(conn, user)

print(fetch_user(conn, user))


