##Webserver import
from flask import Flask, render_template
app = Flask(__name__)

##Connection to blog posts database
import sqlite3
def DBConnect(type):
    connection = sqlite3.connect('./data/blog.db')
    cursor = connection.cursor()
    
    ##Depending on the type of query sent
    match type:
        ##Single Response
        case "select-one":
            return "one"
        
        ##Multi response
        case "select-many":
            cursor.execute("SELECT * FROM Posts")
            rows = cursor.fetchall()
            connection.commit()
            connection.close()
            return render_template("index.html", rows=rows, rowsLen=len(rows))
        
        ##Insert into table
        case "insert":
            cursor.execute("INSERT INTO Posts (title, subtitle, content, image) VALUES ('Starting My Blog', '28/09/2024', 'Test', '1.jpg')")
        ##Create table
        case "create":
            cursor.execute("CREATE TABLE Posts (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL, subtitle TEXT NOT NULL, content TEXT NOT NULL, image TEXT NOT NULL)")

    
    connection.commit()
    connection.close()
    
@app.route("/")
def home():
    #DBConnect("select-many")
    return render_template("post.html")