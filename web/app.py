# Vulnerable Flask App
from flask import Flask, request
import sqlite3
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to the Blind SQLi Lab</h1> <p>Try /search?id=1</p> <p>You can also specify your custom DNS server as follows: /search?set-dns=172.20.53.53&id=1</p>"

@app.route('/search')
def search():
    q = request.args.get('id', '1')
    custom_dns = request.args.get('set-dns')

    con = sqlite3.connect("test.db")
    cur = con.cursor()
    query = f"SELECT hostname FROM local_site WHERE id = {q}"
    print(f"[QUERY] {query}")
    
    try:
        cur.execute(query)
        domain = cur.fetchone()[0]
        
        if custom_dns:
            command = f"nslookup {domain} {custom_dns}"
        else:
            command = f"nslookup {domain}"
        
        print(f"[COMMAND] {command}")
        os.system(command)
        return f"<h1>Lookup Sent</h1><p>Using DNS: {custom_dns or 'default'}</p>"
    except Exception as e:
        return f"<h1>Error</h1><pre>{str(e)}</pre>"

if __name__ == '__main__':
    if not os.path.exists("test.db"):
        con = sqlite3.connect("test.db")
        cur = con.cursor()
        cur.execute("CREATE TABLE local_site (id INTEGER PRIMARY KEY, hostname TEXT);")
        cur.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, password TEXT);")
        cur.execute("INSERT INTO local_site (hostname) VALUES ('www.google.it');")
        cur.execute("INSERT INTO users (username, password) VALUES ('admin', 'supersecret');")
        con.commit()

    app.run(host="0.0.0.0", port=5000)

