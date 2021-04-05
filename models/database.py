from cs50 import SQL
# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///birthdays.db")

db.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER, username TEXT NOT NULL, hash TEXT NOT NULL, PRIMARY KEY(id))")
db.execute("CREATE UNIQUE INDEX IF NOT EXISTS username ON users (username);")
db.execute("""CREATE TABLE IF NOT EXISTS birthdays (id INTEGER, user_id INTEGER NOT NULL, name TEXT NOT NULL,
month INTEGER NOT NULL, day INTEGER NOT NULL, PRIMARY KEY(id), FOREIGN KEY(user_id) REFERENCES users(id))""")
db.execute("""CREATE TABLE IF NOT EXISTS shared (id INTEGER, sender INTEGER NOT NULL, receiver INTEGER NOT NULL,
name TEXT NOT NULL, month INTEGER NOT NULL, day INTEGER NOT NULL, PRIMARY KEY(id),
FOREIGN KEY(sender) REFERENCES users(id), FOREIGN KEY(receiver) REFERENCES users(id))""")