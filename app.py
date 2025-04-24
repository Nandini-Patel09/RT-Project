from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import os
print("Templates directory:", os.path.join(os.getcwd(), 'templates'))

app = Flask(__name__, template_folder='templates')
app.secret_key = 'your_secret_key'

# In-memory storage (use DB in production)
users = {}
expenses = {}
trips = {}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = users.get(email)
        if user and check_password_hash(user['password'], password):
            session['user'] = email
            return redirect(url_for('plan_trip'))
        return "Invalid credentials"
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = generate_password_hash(request.form['password'])
        users[email] = {'password': password}
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/plan_trip', methods=['GET', 'POST'])
def plan_trip():
    if 'user' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        trip_data = {
            'destination': request.form['destination'],
            'duration': request.form['duration'],
            'group_size': request.form['group_size'],
        }
        trips[session['user']] = trip_data
        return jsonify({'message': 'Trip planned successfully', 'trip': trip_data})
    return render_template('PlanTrip.html')

@app.route('/expense_manager', methods=['GET', 'POST'])
def expense_manager():
    if 'user' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        item = request.form['item']
        amount = float(request.form['amount'])
        expenses.setdefault(session['user'], []).append({'item': item, 'amount': amount})
        return jsonify({'message': 'Expense added', 'expenses': expenses[session['user']]})
    return render_template('expensemanager.html', expenses=expenses.get(session['user'], []))

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
