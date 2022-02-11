# Importing modules 
from flask import Flask, render_template

# Creating a Flask object
app = Flask(__name__)

# static routes
# use route() decorator before each view function to create association of URL route with that view function
# home() view function corresponds to the route "/"
@app.route("/") 
def home():
    return "Welcome to the HomePage!"

# we use the variable rule: /<my_name> This variable is then passed as a parameter to the greetings() function in line #16. 
# Finally, the variable my_name is then used in line #19 to return a greeting to the user.
@app.route("/<my_name>")
def greatings(my_name):
    """View function to greet the user by name."""
    return "Welcome "+ my_name +"!"

@app.route('/square/<int:number>')
def show_square(number):
    """View that shows the square of the number passed by URL"""
    return "Square of "+ str(number) +" is: "+ str(number * number) 

@app.route("/educative")
def learn():
    return "Happy Learning at Educative!"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)