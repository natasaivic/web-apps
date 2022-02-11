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

    # if form.is_submitted():
    #     print("Submitted.")
    
    # if form.validate():
    #     print("Valid.")

    # if form.validate_on_submit():
    #    print("Submitted and Valid.")

    if form.validate_on_submit():
        for u_email, u_password in users.items():
            if u_email == form.email.data and u_password == form.password.data:
                return render_template("login.html", message ="Successfully Logged In")
        return render_template("login.html", form = form, message ="Incorrect Email or Password")
    

    # if form.validate_on_submit():
    #     print("Submitted and Valid.")
    #     print("Email:", form.email.data)
    #     print("Password:", form.password.data)
    # elif form.errors:
    #     print(form.errors.items())
    #     print(form.email.errors)
    #     print(form.password.errors)

    # if request.method == "POST":
    #     email = request.form["email"]
    #     password = request.form["password"]
    #     if email in users and users[email] == password:
    #         return render_template("login.html", message ="Successfully Logged In")
    #     return render_template("login.html", message ="Incorrect Email or Password")
    return render_template("login.html", form=form)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)