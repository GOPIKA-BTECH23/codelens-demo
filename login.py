   import sqlite3

   PASSWORD = "admin123"

   def get_user(name):
       conn = sqlite3.connect("app.db")
       return conn.execute("SELECT * FROM users WHERE name = '" + name + "'").fetchall()
