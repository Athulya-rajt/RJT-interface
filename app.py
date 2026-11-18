from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "secret123"


# ---------------- HOME ----------------
@app.route('/')
def home():
    # Always open login first
    if 'user' in session:
        return redirect('/dashboard')
    return redirect('/login')


# ---------------- LOGIN ----------------
@app.route('/login', methods=['GET', 'POST'])
def login():

    # If already logged in, go to dashboard
    if 'user' in session:
        return redirect('/dashboard')

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == "admin" and password == "admin123":
            session['user'] = username
            return redirect('/dashboard')

        return render_template('login.html', error="Invalid username or password")

    return render_template('login.html')


# ---------------- DASHBOARD ----------------
@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect('/login')

    return render_template('index.html')


# ---------------- HISTORY ----------------
@app.route('/history')
def history():
    if 'user' not in session:
        return redirect('/login')

    return render_template('history.html')


# ---------------- REPORTS ----------------
@app.route('/reports')
def reports():
    if 'user' not in session:
        return redirect('/login')

    return render_template('reports.html')


# ---------------- SETTINGS ----------------
@app.route('/settings')
def settings():
    if 'user' not in session:
        return redirect('/login')

    return render_template('settings.html')


# ---------------- ABOUT ----------------
@app.route('/about')
def about():
    if 'user' not in session:
        return redirect('/login')

    return render_template('about.html')


# ---------------- RESULT ----------------
@app.route('/result')
def result():
    if 'user' not in session:
        return redirect('/login')

    return render_template('result.html')


# ---------------- LOGOUT ----------------
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')


if __name__ == '__main__':
    app.run(debug=True)