import sqlite3
from datetime import datetime
import exel
# Connect to the SQLite database (or create it if it doesn't exist)
def connecttothedatabase():
    conn = sqlite3.connect('daily_counter.db')
    c = conn.cursor()

    # Table for products data
    c.execute('''CREATE TABLE IF NOT EXISTS workers (
                id INTEGER PRIMARY KEY,
                
                name TEXT,
                pass TEXT,
                username TEXT

                )''')
    conn.commit()

def d_count(cursor, conn):
    # Get today's date
    temppp , jdjd , hd = exel.initcoutnt()
    bid =[]
    # today = datetime.now().strftime('%Y-%m-%d')
    temp= []
    for e, i in enumerate(jdjd):
        temp.append(i)
        temp.append(hd[e])
        bid.append(temp)
        temp = []
    # # Check if there's an entry for today
    # cursor.execute('SELECT count FROM daily_counts WHERE date = ?', (today,))
    # row = cursor.fetchone()
    
    # if row is None:
    #     # If no entry for today, create one with count = 1
    #     cursor.execute('INSERT INTO daily_counts (date, count) VALUES (?, ?)', (today, 0+temppp))
    #     current_count = 0 +temppp
    # else:
    current_count = temppp
         
    # Commit the changes
    # conn.commit()

    
    return current_count ,bid

def incremeddnt_count(cursor, conn):
    # Get today's date
    today = datetime.now().strftime('%Y-%m-%d')
    
    # Check if there's an entry for today
    cursor.execute('SELECT count FROM daily_counts WHERE date = ?', (today,))
    row = cursor.fetchone()
    
    if row is None:
        # If no entry for today, create one with count = 1
        cursor.execute('INSERT INTO daily_counts (date, count) VALUES (?, ?)', (today, -1))
        current_count = 1
    else:
        # If an entry exists, increment the count
        current_count = row[0] - 1
        cursor.execute('UPDATE daily_counts SET count = ? WHERE date = ?', (current_count, today))
    
    # Commit the changes
    conn.commit()
    
    return current_count
connecttothedatabase()