# app.py
from flask import Flask, request, session, redirect, url_for, render_template, flash,redirect, url_for
import psycopg2  # pip install psycopg2
import psycopg2.extras
import re
import os
import json
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "cairocoders-ednalan"

DB_HOST = "localhost"
DB_NAME = "sampledb"
DB_USER = "postgres"
DB_PASS = "22882288"

conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)


@app.route("/")
def home():
    # Check if user is loggedin
    if "loggedin" in session:
        # User is loggedin show them the home page
        return render_template("home.html", username=session["username"])
    # User is not loggedin redirect to login page
    return redirect(url_for("login"))


@app.route("/index")
def about():
    # Check if user is loggedin
    if "loggedin" in session:
        # User is loggedin show them the home page
        return render_template("about.html", username=session["username"])
    # User is not loggedin redirect to login page
    return redirect(url_for("index"))


# @app.route("/about")
# def hackathon():
#     # Check if user is logged in
#     if "loggedin" in session:
#         # User is logged in, show them the home page
#         return render_template(
#             "/contest/hackathon_home.html", username=session["username"]
#         )

#     # User is not logged in, redirect to the login page
#     return redirect(url_for("login"))




def submit_feedback():
    name = request.form.get('name')
    email = request.form.get('email')
    feedback = request.form.get('feedback')

    # Insert feedback into the database
    conn = psycopg2.connect(
        host="localhost",
        dbname="sampledb",
        user="postgres",
        password="22882288"
    )
    cur = conn.cursor()
    cur.execute(
        sql.SQL("INSERT INTO feedbacks (name, email, feedback) VALUES ({}, {}, {})")
        .format(sql.Literal(name), sql.Literal(email), sql.Literal(feedback))
    )
    conn.commit()
    cur.close()
    conn.close()

    return redirect(url_for('login'))

@app.route("/about", methods=["GET", "POST"])
def hackathon():
    # Check if user is logged in
    if "loggedin" in session:
        if request.method == "POST":
            # User submitted the feedback form
            name = request.form["name"]
            email = request.form["email"]
            feedback_text = request.form["feedback"]

            # Now, you can store this feedback in the database
            insert_feedback(name, email, feedback_text)

            return render_template(
                "/contest/hackathon_home.html", username=session["username"]
            )

        # User is logged in, show them the home page
        return render_template(
            "/contest/hackathon_home.html", username=session["username"]
        )

    # User is not logged in, redirect to the login page
    return redirect(url_for("login"))




@app.route("/daily")
def daily():
    # Check if user is logged in
    if "loggedin" in session:
        # User is logged in, show them the home page
        return render_template(
            "/contest/daily.html", username=session["username"]
        )

    # User is not logged in, redirect to the login page
    return redirect(url_for("login")) 


@app.route("/weekly")
def weekly():
    # Check if user is logged in
    if "loggedin" in session:
        # User is logged in, show them the home page
        return render_template(
            "/contest/weekly.html", username=session["username"]
        )

    # User is not logged in, redirect to the login page
    return redirect(url_for("login"))       
@app.route("/learning")
def learning():
    # Check if user is logged in
    if "loggedin" in session:
        # User is logged in, show them the home page
        return render_template(
            "learn.html", username=session["username"]
        )

    # User is not logged in, redirect to the login page
    return redirect(url_for("login")) 

@app.route("/workshop")
def workshop():
    # Check if user is logged in
    if "loggedin" in session:
        # User is logged in, show them the home page
        return render_template(
            "/workshop/workshop_front.html", username=session["username"]
        )

    # User is not logged in, redirect to the login page
    return redirect(url_for("login")) 


@app.route("/python_exercise")
def python():
    # Check if user is logged in
    if "loggedin" in session:
        # User is logged in, show them the home page
        return render_template(
            "/question/python.html", username=session["username"]
        )

    # User is not logged in, redirect to the login page
    return redirect(url_for("login")) 



@app.route("/workshops")
def workshops():
    # Check if user is logged in
    if "loggedin" in session:
        # User is logged in, show them the home page
        return render_template(
            "/workshop/workshop.html", username=session["username"]
        )

    # User is not logged in, redirect to the login page
    return redirect(url_for("login"))   



@app.route("/project")
def project():
    # Check if user is logged in
    if "loggedin" in session:
        # User is logged in, show them the home page
        return render_template(
            "/workshop/project.html", username=session["username"]
        )

    # User is not logged in, redirect to the login page
    return redirect(url_for("login"))     



@app.route("/carrier")
def carrier():
    # Check if user is logged in
    if "loggedin" in session:
        # User is logged in, show them the home page
        return render_template(
            "/workshop/carrier.html", username=session["username"]
        )

    # User is not logged in, redirect to the login page
    return redirect(url_for("login"))  


@app.route("/exercise")
def exercise():
    # Check if user is logged in
    if "loggedin" in session:
        # User is logged in, show them the home page
        return render_template(
            "exercise.html", username=session["username"]
        )

    # User is not logged in, redirect to the login page
    return redirect(url_for("login"))  



    



@app.route('/contacts', methods=['GET', 'POST'])
def contacts():
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    success_message = None

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message_text = request.form['message']

        # Store the message in the database
        cursor.execute(
            "INSERT INTO messages (name, email, message) VALUES (%s, %s, %s)",
            (name, email, message_text)
        )
        conn.commit()

        success_message = f'Thank you, {name}! Your message has been sent successfully.'

    return render_template('/workshop/contact.html', success_message=success_message)           



       


@app.route("/hackathon")
def blog():
    # Check if user is logged in
    if "loggedin" in session:
        # User is logged in, show them the home page
        return render_template(
            "blog.html", username=session["username"]
        )

    # User is not logged in, redirect to the login page
    return redirect(url_for("login")) 


@app.route("/hackathons")
def hackathons():
    # Check if user is logged in
    if "loggedin" in session:
        # User is logged in, show them the home page
        return render_template(
            "/contest/hackathon.html", username=session["username"]
        )

    # User is not logged in, redirect to the login page
    return redirect(url_for("login"))  


@app.route("/practice")
def practice():
    # Check if user is logged in
    if "loggedin" in session:
        # User is logged in, show them the home page
        return render_template(
            "practice.html", username=session["username"]
        )

    # User is not logged in, redirect to the login page
    return redirect(url_for("login"))      



       



@app.route('/contact', methods=['GET', 'POST'])
def contact():
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    success_message = None

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message_text = request.form['message']

        # Store the message in the database
        cursor.execute(
            "INSERT INTO messages (name, email, message) VALUES (%s, %s, %s)",
            (name, email, message_text)
        )
        conn.commit()

        success_message = f'Thank you, {name}! Your message has been sent successfully.'

    return render_template('contact.html', success_message=success_message)



@app.route('/registration', methods=['POST'])
def registration():
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.method == 'POST':
        team_lead_name = request.form['name']
        team_members = request.form['team_members']
        email = request.form['email']
        college_name = request.form['college_name']

        # Store the form data in the PostgreSQL database
        cursor.execute(
            "INSERT INTO registrations (team_lead_name, team_members, email, college_name) VALUES (%s, %s, %s, %s)",
            (team_lead_name, team_members, email, college_name)
        )
        conn.commit()

        success_message = f'Thank you, {team_lead_name}! Your registration has been successfully saved.'
        return render_template('index.html', success_message=success_message)

    return render_template('index.html')  


@app.route("/login/", methods=["GET", "POST"])
def login():
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    # Check if "username" and "password" POST requests exist (user submitted form)
    if (
        request.method == "POST"
        and "username" in request.form
        and "password" in request.form
    ):
        username = request.form["username"]
        password = request.form["password"]
        print(password)

        # Check if account exists using MySQL
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        # Fetch one record and return result
        account = cursor.fetchone()

        if account:
            password_rs = account["password"]
            print(password_rs)
            # If account exists in users table in out database
            if check_password_hash(password_rs, password):
                # Create session data, we can access this data in other routes
                session["loggedin"] = True
                session["id"] = account["id"]
                session["username"] = account["username"]
                # Redirect to home page
                return redirect(url_for("home"))
            else:
                # Account doesnt exist or username/password incorrect
                flash("Incorrect username/password")
        else:
            # Account doesnt exist or username/password incorrect
            flash("Incorrect username/password")

    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    # Check if "username", "password" and "email" POST requests exist (user submitted form)
    if (
        request.method == "POST"
        and "username" in request.form
        and "password" in request.form
        and "email" in request.form
    ):
        # Create variables for easy access
        fullname = request.form["fullname"]
        username = request.form["username"]
        password = request.form["password"]
        email = request.form["email"]

        _hashed_password = generate_password_hash(password)

        # Check if account exists using MySQL
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        account = cursor.fetchone()
        print(account)
        # If account exists show error and validation checks
        if account:
            flash("Account already exists!")
        elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            flash("Invalid email address!")
        elif not re.match(r"[A-Za-z0-9]+", username):
            flash("Username must contain only characters and numbers!")
        elif not username or not password or not email:
            flash("Please fill out the form!")
        else:
            # Account doesnt exists and the form data is valid, now insert new account into users table
            cursor.execute(
                "INSERT INTO users (fullname, username, password, email) VALUES (%s,%s,%s,%s)",
                (fullname, username, _hashed_password, email),
            )
            conn.commit()
            flash("You have successfully registered!")
    elif request.method == "POST":
        # Form is empty... (no POST data)
        flash("Please fill out the form!")
    # Show registration form with message (if any)
    return render_template("register.html")


@app.route("/logout")
def logout():
    # Remove session data, this will log the user out
    session.pop("loggedin", None)
    session.pop("id", None)
    session.pop("username", None)
    # Redirect to login page
    return redirect(url_for("login"))


@app.route("/profile")
def profile():
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    # Check if user is loggedin
    if "loggedin" in session:
        cursor.execute("SELECT * FROM users WHERE id = %s", [session["id"]])
        account = cursor.fetchone()
        # Show the profile page with account info
        return render_template("profile.html", account=account)
    # User is not loggedin redirect to login page
    return redirect(url_for("login"))














db_connection = {
    'host': 'localhost',
    'database': 'sampledb',
    'user': 'postgres',
    'password': '22882288'
}

# Function to initialize the database
def initialize_database():
    connection = psycopg2.connect(**db_connection)
    cursor = connection.cursor()

    # Create a table to store quiz results if not exists
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS quiz_results (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255),
            email VARCHAR(255),
            score INT
        );
    ''')

    connection.commit()
    connection.close()

# Initialize the database on application startup
initialize_database()

# Load quiz questions from JSON file
questions_path = os.path.join(app.root_path, 'static', 'questions.json')

# Load quiz questions from JSON file
with open(questions_path) as f:
    questions = json.load(f)


# Quiz route
@app.route('/quiz/index')
def quiz():
    return render_template('index.html', questions=questions)

# Results route
@app.route('/quiz/index/results', methods=['POST'])
def results():
    name = request.form['name']
    email = request.form['email']
    score = 0

    for question in questions:
        user_answer = request.form.get(str(question['id']))
        if user_answer and user_answer == question['answer']:
            score += 1

    # Store quiz results in the database
    connection = psycopg2.connect(**db_connection)
    cursor = connection.cursor()
    cursor.execute('''
        INSERT INTO quiz_results (name, email, score)
        VALUES (%s, %s, %s);
    ''', (name, email, score))
    connection.commit()
    connection.close()

    return redirect(url_for('quiz'))
















    
if __name__ == "__main__":
    app.run(debug=True)
