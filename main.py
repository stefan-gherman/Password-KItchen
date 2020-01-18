from flask import Flask, redirect, request, render_template, url_for
import hasher
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def return_home():
    return render_template("index.html", status="default")


@app.route('/hash', methods=['GET', 'POST'])
def hash_password():
    if request.method == 'POST':
        password = request.form['password']
        hashed_password = hasher.hash_pw(password)
        print(hashed_password)
        return render_template("index.html", status="default", show_hash=hashed_password, password=password)

@app.route('/dehash', methods = ['GET', 'POST'])
def check_hash():
    if request.method == 'POST':
        password = request.form['password_verif']
        hashed = request.form['hash_verif']
        truth = hasher.check_pw(password, hashed)
        if truth is True:
            return render_template("index.html", status="checked", hash=hashed, password_verif=password)
        else:
            return render_template("index.html", status="failed", hash=hashed, password_verif=password)
if __name__ == "__main__":
    app.run(debug=True)
