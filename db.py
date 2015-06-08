import sqlite3
import random
import textwrap

import oblique_strategies

max_line_length = 30

def restore_oblique_table():
    con = sqlite3.connect('dontpanic.db')
    with con:
        cur = con.cursor()
        cur.execute("DROP TABLE IF EXISTS oblique")
        cur.execute('''CREATE TABLE oblique
                     (id INTEGER PRIMARY KEY, 
                      quote TEXT NOT NULL)''')
        cur.executemany("INSERT INTO oblique(quote) VALUES (?)", oblique_strategies.strategies)

def print_random_entry():
    entry = random.randint(0, len(oblique_strategies.strategies))
    con = sqlite3.connect('dontpanic.db')
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM oblique WHERE id=?", (entry,))
#        cur.execute("SELECT * FROM oblique")
        row = cur.fetchone()
        quote = '\n'.join(textwrap.wrap(row[1], max_line_length))
        print quote

if __name__ == "__main__":
    #print oblique_strategies.strategies
    restore_oblique_table()
    print_random_entry()
    
