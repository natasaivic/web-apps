from flask import Flask, render_template
from flask import request
from forms import LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'dfewfew123213rwdsgert34tgfd1234trgf'

users = {
    "ivicsnatasa@email.com": "bilosta",
    "popovicsnatasa@email.com": "radenkovic"
}

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    # if request.method == "POST":
    #     email = request.form["email"]
    #     password = request.form["password"]
    #     if email in users and users[email] == password:
    #         return render_template("login.html", message ="Successfully Logged In")
    #     return render_template("login.html", message ="Incorrect Email or Password")
    return render_template("login.html", form=form)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)