from cs50 import SQL
# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

db.execute("""CREATE TABLE IF NOT EXISTS 'balances' ('id' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
                        'user_id' INTEGER NOT NULL, 'symbol' TEXT NOT NULL, 'shares' INTEGER NOT NULL, 
                        FOREIGN KEY(user_id) REFERENCES users(id))""")
db.execute("CREATE UNIQUE INDEX IF NOT EXISTS unique_balances_user_id_symbol ON balances (user_id, symbol)")
db.execute("""CREATE TABLE IF NOT EXISTS 'history' ('id' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
                        'user_id' INTEGER NOT NULL, 'symbol' TEXT NOT NULL, 'shares' INTEGER NOT NULL, 'price' NUMERIC NOT NULL, 
                        'created_at' DATETIME  NOT NULL DEFAULT CURRENT_TIMESTAMP, FOREIGN KEY(user_id) REFERENCES users(id))""")
db.execute("CREATE INDEX IF NOT EXISTS index_histoy_user_id ON balances (user_id)")