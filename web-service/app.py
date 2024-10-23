from flask import Flask, jsonify, request, render_template, redirect, url_for
import sqlite3

app = Flask(__name__)

# Function to connect to the database
def connect_db():
    return sqlite3.connect('database.db')

# Function to initialize the database and create the table if it doesn't exist
def init_db():
    conn = connect_db()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            role TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Home route - displaying the user list
@app.route('/')
def home():
    conn = connect_db()
    cursor = conn.execute('SELECT * FROM users')
    users = cursor.fetchall()
    conn.close()
    return render_template('index.html', users=users)

# API route to get all users
@app.route('/api/users', methods=['GET'])
def get_users():
    conn = connect_db()
    cursor = conn.execute('SELECT * FROM users')
    users = [
        {"id": row[0], "name": row[1], "age": row[2], "role": row[3]} 
        for row in cursor.fetchall()
    ]
    conn.close()
    return jsonify(users)

# API route to add a new user
@app.route('/api/users', methods=['POST'])
def add_user():
    data = request.get_json()
    name = data['name']
    age = data['age']
    role = data['role']

    conn = connect_db()
    conn.execute('INSERT INTO users (name, age, role) VALUES (?, ?, ?)', (name, age, role))
    conn.commit()
    conn.close()
    
    return jsonify({"message": "User added successfully!"})

# API route to update a user
@app.route('/api/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    name = data['name']
    age = data['age']
    role = data['role']
    
    conn = connect_db()
    conn.execute('UPDATE users SET name = ?, age = ?, role = ? WHERE id = ?', (name, age, role, user_id))
    conn.commit()
    conn.close()
    
    return jsonify({"message": "User updated successfully!"})

# API route to delete a user
@app.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    conn = connect_db()
    conn.execute('DELETE FROM users WHERE id = ?', (user_id,))
    conn.commit()
    conn.close()
    
    return jsonify({"message": "User deleted successfully!"})

# Frontend route to add a new user via form
@app.route('/add_user', methods=['POST'])
def add_user_form():
    name = request.form['name']
    age = request.form['age']
    role = request.form['role']

    conn = connect_db()
    conn.execute('INSERT INTO users (name, age, role) VALUES (?, ?, ?)', (name, age, role))
    conn.commit()
    conn.close()
    
    return redirect(url_for('home'))

if __name__ == '__main__':
    # Initialize the database (create table if it doesn't exist)
    init_db()

    # Run the Flask app
    app.run(debug=True)
