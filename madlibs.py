"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    "awesome",
    "terrific",
    "fantastic",
    "neato",
    "fantabulous",
    "wowza",
    "oh-so-not-meh",
    "brilliant",
    "ducky",
    "coolio",
    "incredible",
    "wonderful",
    "smashing",
    "lovely",
]


@app.route("/")
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route("/hello")
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route("/greet")
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html", 
                            person=player, 
                            compliment=compliment)


@app.route("/game")
def show_madlib_form():
    """Get user response to yes or no question on 
    Would you like to play a game? form"""

    player = request.args.get("person")
    user_choice = request.args.get("yes-or-no")

    if user_choice == "yes":
        return render_template("game.html", 
                                person=player)
    else: 
        return render_template("goodbye.html", 
                                person=player)    

    
@app.route("/madlib")
def show_madlib():
    """Show user their MadLibs-style story."""
    
    color_list = request.args.getlist("color")
    noun = request.args.get("noun")
    person = request.args.get("person")
    adjective = request.args.get("adjective")

    return render_template("madlib.html", 
                            color_list=color_list, 
                            noun=noun, person=person, 
                            adjective=adjective)


if __name__ == "__main__":
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True, host="0.0.0.0")
