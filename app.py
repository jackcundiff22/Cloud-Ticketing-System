from flask import Flask, request, render_template, redirect, session 
from datetime import datetime
import sqlite3

app = Flask(__name__)
app.secret_key = "change-this-later"

def init_db():
  conn = sqlite3.connect("tickets.db")
  cursor = conn.cursor()

  cursor.execute("""
    CREATE TABLE IF NOT EXISTS tickets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,
    status TEXT,
    priority TEXT,
    issue TEXT
    )
  """)
  conn.commit()
  conn.close()

@app.route("/login", methods=["GET", "POST"])
def login():
     if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username == "admin" and password == "password123":
             session["logged_in"] = True
             return redirect("/")
        
        return "Invalid credentials. Please try again."
     
     return render_template("login.html")

@app.route("/", methods=["GET", "POST"])
def home():
        
        if not session.get("logged_in"):
             return redirect("/login")

        if request.method == "POST":
            priority = request.form["priority"]
            ticket = request.form["ticket"]
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
            conn = sqlite3.connect("tickets.db")
            cursor = conn.cursor()

            cursor.execute("""INSERT INTO tickets (timestamp, status, priority, issue) VALUES (?, ?, ?, ?)""",
            (timestamp, "OPEN", priority, ticket))

            conn.commit()
            conn.close()

        status_filter = request.args.get("status")

        conn = sqlite3.connect("tickets.db")
        cursor = conn.cursor()


        if status_filter:
           cursor.execute("SELECT id, timestamp, status, priority, issue FROM tickets WHERE status = ?",
           (status_filter,)
           )

        else:
           cursor.execute("SELECT id, timestamp, status, priority, issue FROM tickets")

        tickets = cursor.fetchall()

        conn.close()

        ticket_list = ""


        for ticket in tickets:
            if ticket[2] == "OPEN":
                action_html = f"""
                <form method="POST" action="/close/{ticket[0]}">
                <button type="submit">Close Ticket</button>

                <form method="POST" action="/delete/{ticket[0]}">
                <button type="submit">Delete Ticket</button>
                </form>
                </form>
                """
            else:
                action_html = f"""<strong>Ticket Closed</strong>"
                <form method="POST" action="/delete/{ticket[0]}">
                <button type="submit">Delete Ticket</button>
                </form> """



            ticket_list += f"""
            <div class='ticket-card'>
                <strong>Ticket #{ticket[0]}</strong><br>
                Time: {ticket[1]}<br>
                Status: {ticket[2]}<br>
                Priority: {ticket[3]}<br>
                Issue: {ticket[4]}<br><br>
                {action_html}


            </div>
            """

        return render_template("index.html", ticket_list=ticket_list)

@app.route("/logout")
def logout():
     session.clear()
     return redirect("/login")

@app.route("/close/<int:ticket_id>", methods=["POST"])
def close_ticket(ticket_id):
        conn =sqlite3.connect("tickets.db")
        cursor = conn.cursor()

        cursor.execute("""UPDATE tickets SET status = ? WHERE id = ? """, ("CLOSED", ticket_id))
        conn.commit()
        conn.close()

        return redirect("/")

@app.route("/delete/<int:ticket_id>", methods=["POST"])
def delete_ticket(ticket_id):

    conn = sqlite3.connect("tickets.db")
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM tickets
        WHERE id = ?
    """, (ticket_id,))

    conn.commit()
    conn.close()

    return redirect("/")

if __name__ == "__main__":
        init_db()
        app.run(host="127.0.0.1", port=5000)
