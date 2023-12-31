
cur.execute('INSERT INTO challenge(RFID, USER, PASS, LEVEL, START_TS) VALUES (?, ?, ?, ?, ?)', (rfid, get_user(rfid), get_pass(rfid), 1, time.time()))

'INSERT INTO challenge(RFID, USER, PASS, LEVEL, START_TS) VALUES (|,,,7;?, ?, ?, ?, ?)', (rfid, get_user(rfid), get_pass(rfid), 1, time.time()))


#!/bin/python

import telnetlib
from hashlib import sha256

def get_user(rfid):
    hash_string = sha256(rfid.encode()).hexdigest()
    # hash_string = sha256(rfid).hexdigest()
    user = 'u0x' + hash_string.lower()[:8]
    return user

def get_rfid(rfid):
    result = []
    for x in range(0,4):
        if rfid[x] < 0x10:
            print(0x00)
            result.append(0x00)
        print(rfid[x])
        result.append(rfid[x])
    return result

def get_pass(rfid):
    bytes_array = bytes.fromhex(rfid)
    hash_bytes = sha256(bytes_array).hexdigest().upper()[:8]
    return hash_bytes

hints1 = ('T11', 'Zhy1')
hints2 = ('T10', 'yOxM')
hints3 = ('A4', 'JYfr06gj')
hints4 =  'Vz5XA'


HOST = 'telnet.tt23.it'
# rfid_id = b'\x04\xeb\xf5\x04' #\xbb\x2a\x81'
rfid_id = '04EBF504' #bb2a81'

used = get_user(rfid_id)
print(used)


tn = telnetlib.Telnet(HOST)
# tn.set_debuglevel(10)

print(tn.read_until(b"Username: "))

tn.write(used.encode() + b'\x0d')
print(tn.read_until(b"Password: "))

password = get_pass(rfid_id)
tn.write(password.encode() + b'\x0d')
tn.interact()
print(tn.read_all())
