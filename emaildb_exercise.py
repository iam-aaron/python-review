import sqlite3
import re

conn = sqlite3.connect('emaildb_exer.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox.txt'
fh = open(fname)
domain_count = dict()

for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    domain = re.findall('@(.+)',pieces[1])[0]
    domain_count[domain] = domain_count.get(domain,0) + 1

for key,value in domain_count.items():
    cur.execute('INSERT INTO Counts (org, count) VALUES (?, ?)', (key,value))
    conn.commit()

sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])


cur.close()
