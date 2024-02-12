from flask import Flask

app = Flask(__name__)


@app.route('/')
def Hello_world():
    return '<h1 style="text-align:center">Hello World</h1>' \
        '<p>This is paragraph</p>' \
        '<img src="https://cdn.pixabay.com/photo/2017/02/20/18/03/cat-2083492_640.jpg" width=200px>'


def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper


def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper


def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper


@app.route('/bye')
@make_bold
@make_emphasis
@make_underlined
def say_bye():
    return "Bye Bye!"


# @app.route('/<path:name>/<int:number>')
@app.route('/<name>/<int:number>')
def greet(name, number):
    return f"Hello there {name}, you are {number} year old!"


if __name__ == "__main__":
    # run app in debug mode.
    app.run(debug=True)

