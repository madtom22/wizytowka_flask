from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello():
    my_name = "Tomek"
    return f'Hello, {my_name}!'

@app.route('/contact', methods=['GET', 'POST'])
def contact():
   if request.method == 'GET':
       print("We received GET")
       return render_template("contact.html")
   elif request.method == 'POST':
       print("We received POST")
       print(request.form)
       return redirect("/")

@app.route('/me')
def me():
    return render_template("me.html")
