from flask import Flask, render_template, request, redirect
from flask_pymongo import PyMongo

app = Flask(__name__)

# Connect to MongoDB
app.config["MONGO_URI"] = "mongodb://localhost:27017/my"
mongo = PyMongo(app)

# Home route
@app.route('/')
def index():
    users = mongo.db.users.find()  # Fetch all users from the database
    return render_template('index.html', users=users)

# Add a new user
@app.route('/add', methods=['POST'])
def add_user():
    name = request.form.get('name')
    age = request.form.get('age')
    if name and age:
        mongo.db.users.insert_one({'name': name, 'age': age})
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
