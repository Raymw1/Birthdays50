from models.database import db

# def sell(id, symbol, shares):
#     symbol = symbol.upper()
#     stock = lookup(symbol)
#     success, message = balances.sell_user_shares(id, symbol, shares)
#     if not success:

#     db.execute("INSERT INTO  history (user_id, symbol, shares, price) VALUES (?, ?, ?, ?)", session["user_id"], symbol, shares * -1, stock["price"])
#     total = stock["price"] * shares
#     row = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])
#     new_cash = row[0]["cash"] + total
#     db.execute("UPDATE  users SET cash = ? WHERE id = ?",  new_cash, session["user_id"])