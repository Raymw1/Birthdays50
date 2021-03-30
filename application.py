import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session, send_file
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from helpers import apology, login_required
from models import database, users
from werkzeug.security import check_password_hash, generate_password_hash

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response



# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = database.db

#  --------------------------------------    WELCOME PAGE     ------------------------------

@app.route("/")
def welcome():
    session.clear()
    wel = True;
    return render_template("index.html", welcome=wel)

#  -------------------------------------     REGISTER PAGE     ------------------------------------------------

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("pwd")
        confirmation = request.form.get("confirmation")
        # Ensure username was submitted
        if not username:
            return apology("Provide a username", 400)

        # Verify username
        if  users.verify_username(username):
            return apology("Provide a username not registered yet", 400)

        # Ensure password was submitted
        elif not password:
            return apology("Provide a password", 400)

        elif password != confirmation:
            return apology("Provide passwords matching", 400)

        new_user_id = users.register(username, password)
        session["user_id"] = new_user_id
        # Redirect user to home page
        return redirect("/index")
    else:
        return render_template("register.html")

#  ---------------------------------    LOGIN PAGE    -----------------------------------

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""
    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("pwd")
        # Ensure username was submitted
        if not username:
            return apology("Provide an username", 403)

        # Ensure password was submitted
        elif not password:
            return apology("Provide a password", 403)

        rows = db.execute("SELECT * FROM users WHERE username = ?", username)
        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], password):
            return apology("Provide a valid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]
        # Redirect user to home page
        return redirect("/index")
    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")

# -------------------------       BIRTHDAYS PAGE --------------------------------

@app.route("/index", methods=["GET", "POST"])
@login_required
def  index():
    if request.method == "POST":
        names = db.execute("SELECT name FROM birthdays WHERE user_id = ?", session["user_id"])
        name = request.form.get("name")
        month = int(request.form.get("month"))
        day = int(request.form.get("day"))
        if len(name) < 3:
            return apology("Provide a name with at least 3 letters", 400)
        for tname in names:
            if name == tname["name"]:
                return apology("Provide a name not used yet", 400)
        if month == 2 and day > 29:
            return apology("Provide a valid day", 400)
        elif (month == 4 or month == 6 or month == 9 or month == 11) and day > 30:
            return apology("Provide a valid day", 400)
        db.execute("INSERT INTO birthdays (user_id, name, month, day) VALUES(?, ?, ?, ?)", session["user_id"], name, month, day)
        return redirect("/index")

    else:
        birthdays = db.execute("SELECT name, day, month FROM birthdays WHERE user_id = ? ORDER BY month, day ASC", session["user_id"])
        return render_template("birthdays.html", birthdays=birthdays)

# @app.route("/")
# @login_required
# def index():
#     user = users.get_user_by_user_id(session["user_id"])
#     rows = balances.get_balances_by_user_id(user["id"])
#     stocks = []
#     for row in rows:
#         balance = row
#         stock = lookup(balance["symbol"])
#         balance["price"] = stock["price"]
#         balance["total"] = stock["price"] * balance["shares"]
#         balance["name"] = stock["name"]
#         stocks.append(balance)
#     total_spent = user["cash"]
#     for balance in stocks:
#         total_spent += balance["total"]
#     # stocks |  shares  |  current price |  total (shares*price)
#     """Show portfolio of stocks"""
#     return render_template("index.html", cash=user["cash"], balances=stocks, spent=total_spent)


# @app.route("/history")
# @login_required
# def history():
#     """Show history of transactions"""
#     rows = hist.get_history_by_user_id(session["user_id"])
#     return render_template("history.html", history=rows)

@app.route("/change_pwd", methods=["GET", "POST"])
def change_password():
    if request.method == "POST":
        # Ensure password was submitted
        if not request.form.get("current_password"):
            return apology("must provide current password", 403)

        if not request.form.get("password"):
            return apology("must provide password", 403)

        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("passwords do not match", 400)

        updated_successfully = users.update_password(session["user_id"], request.form.get("current_password"), request.form.get("password"))
        if not updated_successfully:
            flash("Invalid current password")
            return render_template("change_password.html")
        # Redirect user to home page
        flash("Password updated successfully")
        return redirect("/")
    else:
        return render_template("change_password.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


# @app.route("/quote", methods=["GET", "POST"])
# @login_required
# def quote():
#     """Get stock quote."""
#     if request.method == "POST":
#         symbol = request.form.get("symbol")
#         if not symbol:
#             return apology("missing symbol", 400)
#         stock = lookup(symbol)
#         if not stock:
#             return apology("invalid symbol", 400)
#         return render_template("quoted.html", stock=stock)
#     else:
#         return render_template("quote.html")


# @app.route("/buy", methods=["GET", "POST"])
# @login_required
# def buy():
#     """Buy shares of stock"""
#     """Get stock quote."""
#     if request.method == "POST":
#         symbol = request.form.get("symbol")
#         shares = int(request.form.get("shares"))
#         if not symbol:
#             return apology("missing symbol", 400)
#         stock = lookup(symbol)
#         if not stock:
#             return apology("invalid symbol", 400)
#         if not shares:
#             return apology("must provide the number of shares", 400)
#         symbol = symbol.upper()
#         total = stock["price"] * shares
#         row = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])
#         cash = row[0]["cash"]
#         if cash < total:
#             return apology("can't afford", 400)
#         row = db.execute("SELECT * FROM balances WHERE id = ? AND  symbol = ?", session["user_id"], symbol)
#         if len(row) < 1:
#             db.execute("INSERT INTO  balances (user_id, symbol, shares) VALUES (?, ?, ?)", session["user_id"], symbol, shares)
#         else:
#             balance = row[0]
#             balance["shares"] += shares
#             db.execute("UPDATE balances SET shares = ? WHERE id = ?", balance["shares"], balance["id"])
#         db.execute("INSERT INTO  history (user_id, symbol, shares, price) VALUES (?, ?, ?, ?)", session["user_id"], symbol, shares, stock["price"])
#         new_cash = cash - total
#         db.execute("UPDATE  users SET cash = ? WHERE id = ?",  new_cash, session["user_id"])
#         flash(f"Bought {shares} of {symbol} successfully", "success")
#         return redirect("/")
#     else:
#         return render_template("buy.html")

# @app.route("/sell", methods=["GET", "POST"])
# @login_required
# def sell():
#     if request.method == "POST":
#         symbol = request.form.get("symbol")
#         shares = int(request.form.get("shares"))
#         if not symbol:
#             return apology("must provide a valid stock symbol", 400)
#         symbol = symbol.upper()
#         stock = lookup(symbol)
#         success, message = balances.sell_user_shares(session["user_id"], symbol, shares)
#         if not success:
#             return apology(message, 400)
#         hist.insert_new_entry(session["user_id"], symbol, shares * -1, stock["price"])
#         users.add_cash(session["user_id"], stock["price"] * shares, shares)
#         flash(f"Sold {shares} of {symbol} successfully", "success")
#         return redirect("/")
#     else:
#         stocks = balances.get_positive_stocks(session["user_id"])
#         return render_template("sell.html", stocks=stocks)


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)

