from flask import Flask, render_template, abort
from forms import SignupForm, LoginForm
from flask import session, redirect, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dfewfew123213rwdsgert34tgfd1234trgf'

"""Information regarding the Pets in the System."""
pets = [
            {"id": 1, "name": "Nelly", "age": "5 weeks", "bio": "I am a tiny kitten rescued by the good people at Paws Rescue Center. I love squeaky toys and cuddles."},
            {"id": 2, "name": "Yuki", "age": "8 months", "bio": "I am a handsome gentle-cat. I like to dress up in bow ties."},
            {"id": 3, "name": "Basker", "age": "1 year", "bio": "I love barking. But, I love my friends more."},
            {"id": 4, "name": "Mr. Furrkins", "age": "5 years", "bio": "Probably napping."}, 
        ]

users = [
            {"id": 1, "full_name": "Pet Rescue Team", "email": "team@pawsrescue.co", "password": "adminpass"},
        ]


@app.route("/")
def home():
    return render_template("home.html", pets=pets)

@app.route("/details/<int:pet_id>")
def pet_details(pet_id):
    pet = None
    for animal in pets:
        if animal["id"] == pet_id:
            pet = animal
    if pet is None:
        abort(404, description="No Pet was Found with the given ID")
    
    return render_template("details.html", pet=pet)

@app.route("/signup", methods=["POST", "GET"])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        new_user = {"id": len(users)+1, "full_name": form.full_name.data, "email": form.email.data, "password": form.password.data}
        users.append(new_user)
        return render_template("signup.html", message = "Successfully signed up")
    
    return render_template("signup.html", form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = None
        for record in users:
            if record["email"] == form.email.data and record["password"] == form.password.data:
                user = record
        if user is None:
            return render_template("login.html", form = form, message = "Wrong Credentials. Please Try Again.")
        else:
            session['user'] = user
            return render_template("login.html", message = "Successfully Logged In!")
    
    return render_template("login.html", form=form)

@app.route("/logout")
def logout():
    if 'user' in session:
        session.pop('user')
    return redirect(url_for('home', _scheme='https', _external=True))

@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    """ """
    app.run(debug=True, host="0.0.0.0", port=3000)