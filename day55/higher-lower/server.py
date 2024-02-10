from flask import Flask
import random

app = Flask(__name__)

random_number = random.randint(0,9)

@app.route('/')
def Hello():
    return '<h1> Guess the number between 0 to 9 <h1>' \
    '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'

@app.route('/<number>')
def guessed_number(number):
    number = int(number)
    if number == random_number:
        return '<h1 style="color: green"> You Got it" <h1>' \
               '<img src=" https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'
    elif number < random_number:
        return '<h1 style="color: red""> Too Low <h1>' \
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
    else:
        return '<h1 style="color: purple""> Too High <h1>' \
               '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'


if __name__ == '__main__':
    app.run(debug=True)