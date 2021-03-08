from models.database import db

def get_balances_by_user_id(id):
    rows = db.execute("SELECT * FROM balances WHERE user_id = ?", id)
    return rows

def sell_user_shares(id, symbol, shares):
    balances = db.execute("SELECT * FROM balances WHERE user_id = ? AND  symbol = ?", id, symbol)
    if len(balances) < 1:
        return False, f"insufficient shares for symbol {symbol}"
    balance = balances[0]
    if shares > balance["shares"]:
        return False, "insufficient shares for sale"
    balance["shares"] -= shares
    db.execute("UPDATE balances SET shares = ? WHERE id = ?", balance["shares"], balance["id"])
    return True, None

def get_positive_stocks(id):
    return db.execute("SELECT * FROM balances WHERE user_id = ? AND shares > 0", id)