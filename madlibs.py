"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]


@app.route('/')
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."



@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("playgame.html")


@app.route('/playgame')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    play_game = request.args.get("game")
    if play_game == "No":
            return render_template("goodbye.html", person=player)
    else:

        return render_template("game.html", person=player)


@app.route('/goodbye')
def goodbye():
    """say goodbye"""

    player = request.args.get("person")

    return render_template("goodbye.html", person=player)


@app.route('/game')
def show_madlib_form():
    player = request.args.get("person")
    name_p = request.args.get("name")
    color_p = request.args.get("color")
    noun_p = request.args.get("noun")
    adj = request.args.get("adjective")

    return render_template("game.html", person=player, name=name_p,
                     color=color_p, noun=noun_p, adjective=adj)


@app.route('/madlib')
def show_madlib():
    player = request.args.get("person")
    name_p = request.args.get("name")
    color_p = request.args.get("color")
    noun_p = request.args.get("noun")
    adj = request.args.get("adjective")

    return render_template("madlib.html", person=player, name=name_p,
    color=color_p, noun=noun_p, adjective=adj)

if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True)
