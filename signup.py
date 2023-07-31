# app.py

from flask import Flask, render_template, request, redirect
import psycopg2

app = Flask(__name__)

# Replace the following with your PostgreSQL database connection details
DB_HOST = "your_postgres_host"
DB_NAME = "your_database_name"
DB_USER = "your_database_user"
DB_PASSWORD = "your_database_password"

def create_connection():
    return psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )

@app.route("/")
def index():
    return render_template("signup.html")

@app.route("/signup", methods=["POST"])
def signup():
    if request.method == "POST":
        # Get user data from the form
        name = request.form.get("name")
        email = request.form.get("email")

        # Connect to the PostgreSQL database
        connection = create_connection()

        # Create a cursor to execute SQL queries
        cursor = connection.cursor()

        # Define the SQL query to insert the user data into the database
        insert_query = "INSERT INTO users (name, email) VALUES (%s, %s)"

        # Execute the query with the user data
        cursor.execute(insert_query, (name, email))

        # Commit the changes to the database
        connection.commit()

        # Close the cursor and connection
        cursor.close()
        connection.close()

        # Redirect to a thank-you page or another page of your choice
        return redirect("/thankyou")

if __name__ == "__main__":
    app.run(debug=True)