import sqlite3
import subprocess
import hashlib
from flask import Flask, request

app = Flask(__name__)

# Bug 1: SQL Injection
@app.route('/user')
def get_user():
    user_id = request.args.get('id')
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE id = " + user_id
    cursor.execute(query)
    return str(cursor.fetchall())

# Bug 2: Command Injection
@app.route('/ping')
def ping_host():
    host = request.args.get('host')
    result = subprocess.check_output("ping -c 1 " + host, shell=True)
    return result

# Bug 3: Weak hashing
def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

# Bug 4: Hardcoded credentials
API_KEY = "sk_live_abc123secretkey456"
DATABASE_PASSWORD = "admin123"

if __name__ == '__main__':
    app.run(debug=True)
