SECRET_KEY = 12
print(SECRET_KEY)
print("hi")
import psycopg2

connection = psycopg2.connect(
    host="localhost",
    database="psycopgtest",
    user="postgres",
    password=None,
)
connection.set_session(autocommit=True)
