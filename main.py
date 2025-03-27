from flask import Flask, render_template
import os

databases = []
databaseName = ""
tableName = ""
query = ""

app = Flask(__name__)

@app.route("/api/upload")
def upload():
    return "<p>Hello, World!</p>"

@app.route("/api/select")
def select():
    return "<p>Hello, World!</p>"

@app.route("/api/delete")
def delete():
    return "<p>Hello, World!</p>"

@app.route("/api/insert")
def insert():
    return "<p>Hello, World!</p>"

@app.route("/api/show")
def show():
    return {"hello": "There"}

@app.route("/")
def main():
    databases = []
    for database in os.listdir(path="databases"):
        if os.path.isfile(f"databases/{database}"):
            databases.append(database)
    print(databases)
    return render_template('index.html', databases=databases)

@app.route("/database")
def database():
    return render_template('database.html')

@app.route("/table")
def table():
    return render_template('table.html')

@app.route("/column")
def column():
    return render_template('column.html')


app.run(debug=True)