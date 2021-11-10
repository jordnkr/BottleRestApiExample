import sqlite3
from bottle import request, route, run
from bottle import post, get, put, delete

@get('/items')
def get_all_items():
    conn = sqlite3.connect('items.db')
    c = conn.cursor()    
    c.execute("SELECT * FROM items order by id")
    result = c.fetchall()
    items = []
    for item in result:
        items.append({'id': item[0], 'item': item[1], 'price': item[2]})
    return {'items': items}

@get('/items/<id:int>')
def get_item(id):
    conn = sqlite3.connect('items.db')
    c = conn.cursor()    
    c.execute("SELECT * FROM items where id=?", (id,))
    result = c.fetchall()
    return {'id': result[0][0], 'item': result[0][1], 'price': result[0][2]}

@post('/items')
def new_item():
    data = request.json
    conn = sqlite3.connect('items.db')
    c = conn.cursor()
    c.execute("INSERT INTO items (item,price) VALUES (?,?)", (data['item'],data['price']))
    conn.commit()
    c.close()
    return data

@put('/items/<id:int>')
def update_item(id):
    data = request.json
    conn = sqlite3.connect('items.db')
    c = conn.cursor()
    c.execute("UPDATE items SET item=?,price=? WHERE id=?", (data['item'],data['price'], id))
    conn.commit()
    c.close()
    return data

@delete('/items/delete/<id:int>')
def delete_item(id):
    conn = sqlite3.connect('items.db')
    c = conn.cursor()
    c.execute("DELETE FROM items WHERE id=?", (id,))
    conn.commit()
    c.close()

    return {}

if __name__ == '__main__':
    run(reloader=True, debug=True)