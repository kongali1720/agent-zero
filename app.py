from flask import Flask, render_template, request, redirect, session
import os
from tools import scan, whois

app = Flask(__name__)
app.secret_key = 'agentzerosecret'

# Dummy credentials
USERNAME = 'admin'
PASSWORD = '1234'

@app.route('/')
def home():
    return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] == USERNAME and request.form['password'] == PASSWORD:
            session['logged_in'] = True
            return redirect('/dashboard')
        else:
            return render_template('login.html', error="Gagal, coba lagi boss!")
    return render_template('login.html')

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if not session.get('logged_in'):
        return redirect('/login')
    result = None
    if request.method == 'POST':
        target = request.form['target']
        action = request.form['action']
        if action == 'whois':
            result = whois.lookup(target)
        elif action == 'scan':
            result = scan.port_scan(target)
    return render_template('dashboard.html', result=result)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')

if __name__ == '__main__':
    app.run(debug=True)
