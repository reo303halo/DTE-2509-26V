from flask import Flask, render_template, redirect, session, request
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_urlsafe(16)

# In-memory users
users = {
    'alice': {'password': 'pass', 'balance': 100}
}

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form.get('username')
        pwd = request.form.get('password')

        if user in users and users[user]['password'] == pwd:
            session['user'] = user
            return redirect('/transfer')

    return render_template('login.html')


@app.route('/transfer', methods=['GET', 'POST'])
def transfer():
    if 'user' not in session:
        return redirect('/login')

    if request.method == 'POST':
        sender = session['user']
        recipient = request.form.get('to')
        amount = int(request.form.get('amount'))

        users[sender]['balance'] -= amount

        message = f"Transferred ${amount} to {recipient}!"
        return render_template(
            'transfer.html',
            balance=users[sender]['balance'],
            message=message
        )

    balance = users[session['user']]['balance']
    return render_template('transfer.html', balance=balance)


if __name__ == '__main__':
    app.run(debug=True)