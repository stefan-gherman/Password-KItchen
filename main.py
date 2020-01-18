from flask import Flask, redirect, request, render_template, url_for
import hasher
app = Flask(__name__)

password = None
@app.route('/', methods=['GET', 'POST'])
def return_home():
    global password
    password=None
    return render_template("index.html", status="default")


@app.route('/hash', methods=['GET', 'POST'])
def hash_password():
    if request.method == 'POST':
        global password
        password = request.form['password']
        hashed_password = hasher.hash_pw(password)
        print("This is the password: ", password)
        return render_template("index.html", status="default", show_hash=hashed_password, password=password)


if __name__ == "__main__":
    app.run(debug=True)
