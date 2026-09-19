from flask import Flask, render_template, request, redirect, session
from cs50 import SQL
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

app.config["SECRET_KEY"] = "dev-secret-key"

db = SQL("sqlite:///tracker.db")


@app.route("/")
def index():

    # User must be logged in
    if "user_id" not in session:
        return redirect("/login")

    # Get only this user's study sessions
    sessions = db.execute(
        "SELECT * FROM sessions WHERE user_id = ? ORDER BY date DESC",
        session["user_id"]
    )

    # Calculate statistics for this user only
    stats = db.execute(
        """
        SELECT
            COUNT(*) AS session_count,
            COALESCE(SUM(minutes), 0) AS total_minutes
        FROM sessions
        WHERE user_id = ?
        """,
        session["user_id"]
    )[0]

    hours = stats["total_minutes"] // 60
    remaining_minutes = stats["total_minutes"] % 60

    return render_template(
        "index.html",
        sessions=sessions,
        stats=stats,
        hours=hours,
        remaining_minutes=remaining_minutes
    )


@app.route("/add", methods=["GET", "POST"])
def add():

    # User must be logged in
    if "user_id" not in session:
        return redirect("/login")

    if request.method == "POST":

        subject = request.form.get("subject")
        minutes = request.form.get("minutes")
        date = request.form.get("date")
        notes = request.form.get("notes")

        if not subject or not minutes or not date:
            return "Missing required fields", 400

        # Add the session and connect it to this user
        db.execute(
            """
            INSERT INTO sessions
            (user_id, subject, minutes, date, notes)
            VALUES (?, ?, ?, ?, ?)
            """,
            session["user_id"],
            subject,
            minutes,
            date,
            notes
        )

        return redirect("/")

    return render_template("add.html")


@app.route("/delete", methods=["POST"])
def delete():

    # User must be logged in
    if "user_id" not in session:
        return redirect("/login")

    session_id = request.form.get("id")

    if not session_id:
        return "Missing session ID", 400

    # Delete the session only if it belongs to this user
    db.execute(
        "DELETE FROM sessions WHERE id = ? AND user_id = ?",
        session_id,
        session["user_id"]
    )

    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if not username or not password or not confirmation:
            return "Missing required fields", 400

        if password != confirmation:
            return "Passwords do not match", 400

        existing_user = db.execute(
            "SELECT * FROM users WHERE username = ?",
            username
        )

        if existing_user:
            return "Username already exists", 400

        password_hash = generate_password_hash(password)

        db.execute(
            "INSERT INTO users (username, hash) VALUES (?, ?)",
            username,
            password_hash
        )

        return redirect("/login")

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        if not username or not password:
            return "Missing username or password", 400

        users = db.execute(
            "SELECT * FROM users WHERE username = ?",
            username
        )

        if len(users) != 1:
            return "Invalid username or password", 400

        user = users[0]

        if not check_password_hash(user["hash"], password):
            return "Invalid username or password", 400

        session["user_id"] = user["id"]

        return redirect("/")

    return render_template("login.html")


@app.route("/logout")
def logout():

    session.clear()

    return redirect("/login")
