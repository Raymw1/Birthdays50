from models.database import db

def get_history_by_user_id(id):
    history = db.execute("SELECT * FROM history WHERE user_id = ?", id)
    return history

def insert_new_entry(id, symbol, shares, price):
    db.execute("INSERT INTO  history (user_id, symbol, shares, price) VALUES (?, ?, ?, ?)", id, symbol, shares, price)