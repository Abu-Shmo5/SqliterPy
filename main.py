from flask import Flask, render_template
import os
import sqlite3
from lib.helper import Helper

################################
#region Helping function
################################

################################
###### Sqlite3 Functions #######
################################
def get_databases():
    return Helper.get_files("databases")

def get_tables(database_name):
    con = sqlite3.connect(f"databases/{database_name}")
    cursor = con.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name!='sqlite_master' AND name!='sqlite_sequence';")
    tables = [table[0] for table in cursor.fetchall()]
    cursor.close()
    return tables

def get_table_schema(database_name, table_name):
    con = sqlite3.connect(f"databases/{database_name}")
    cursor = con.cursor()
    cursor.execute(f"PRAGMA table_xinfo({table_name})")
    columns = []
    for column in cursor.fetchall():
        columns.append({"cid": column[0], "name": column[1], "type": column[2], "notnull": column[3], "dflt_value": column[4], "pk": column[5], "hidden": column[6]})
    cursor.close()
    return columns
    

def get_data(database_name, table_name, select="*"):
    pass

################################
####### Config Functions #######
################################
def get_fonts():
    fonts = []
    for font in Helper.get_files("static/font/"):
        font_parts = font.split(".")
        fonts.append({"name": font_parts[0], "file_name": font_parts[1]})
    return fonts

################################
#endregion
################################

app = Flask(__name__)

################################
#region API Pages
################################

################################
###### Sqlite3 Functions #######
################################
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

@app.route("/api/export")
def export():
    return "<p>Hello, World!</p>"

@app.route("/api/show")
def show():
    databases = get_databases()
    return {"hello": "There", "databases": len(databases)}

################################
#endregion
################################

################################
#region View Pages
################################

@app.route("/")
def main():
    databases = get_databases()
    return render_template('index.html', databases=databases)

@app.route("/config")
def config():
    return render_template('config.html', fonts=get_fonts())

@app.route("/database/<database_name>")
def database(database_name):
    tables = get_tables(database_name)
    return render_template('database.html', database_name=database_name, tables=tables)

@app.route("/table/<database_name>/<table_name>")
def table(database_name, table_name):
    columns = get_table_schema(database_name, table_name)
    return render_template('table.html', database_name=database_name, table_name=table_name, columns=columns)

@app.route("/column/<database_name>/<table_name>/<column_name>")
def column(database_name, table_name, column_name):
    return render_template('column.html', database_name=database_name, table_name=table_name, column_name=column_name)

################################
#endregion
################################

app.run(debug=True)