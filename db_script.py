import sqlite3
 
conn = sqlite3.connect('items.db')
conn.execute("CREATE TABLE items (id INTEGER PRIMARY KEY, item TEXT, price INTEGER)")
conn.execute("INSERT INTO items (item, price) VALUES ('car','20000')")
conn.execute("INSERT INTO items (item, price) VALUES ('chair','450')")
conn.execute("INSERT INTO items (item, price) VALUES ('PC','999')")
conn.execute("INSERT INTO items (item, price) VALUES ('shovel','35')")
conn.commit()