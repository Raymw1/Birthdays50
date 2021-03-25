def apology(message, code=400):
    """Render message as an apology to user."""
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=escape(message)), code

def checkMonthDays(month, day):
    if month == 2 and day > 29:
        return apology("Provide a valid day", 403)
    elif month == [4, 6, 9, 11] and day > 30:
        return apology("Provide a valid day", 403)