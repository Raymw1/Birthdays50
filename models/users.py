from models.database import db
from helpers import apology, login_required, usd
from werkzeug.security import check_password_hash, generate_password_hash

def get_user_by_user_id(id):
    users = db.execute("SELECT * FROM users WHERE id = ?", id)
    if len(users) > 0:
        return users[0]
    else:
        return None


def register(username, password):
    hashed_password = generate_password_hash(password)
    # Query database for username
    new_user_id = db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", username, hashed_password)
    
    return new_user_id

def update_password(id, current_password, password):
    user = get_user_by_user_id(id)
    if not check_password_hash(user["hash"], current_password):
        return None
    hashed_password = generate_password_hash(password)
    # Query database for username
    new_user_id = db.execute("UPDATE users SET hash = ? WHERE id = ?", hashed_password, id)
    return True

# def add_cash(id, amount, shares):
#     row = get_user_by_user_id(id)
#     new_cash = row["cash"] + amount
#     db.execute("UPDATE  users SET cash = ? WHERE id = ?",  new_cash, id)

def verify_username(username):
    usernamess = []
    usernames = db.execute("SELECT username FROM users")
    for name in usernames:
        usernamess.append(name["username"])
    if  username in usernamess:
        return True
    else:
        return False