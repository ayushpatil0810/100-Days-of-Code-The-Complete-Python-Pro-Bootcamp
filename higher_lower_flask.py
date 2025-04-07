import random

from flask import Flask

app = Flask(__name__)


@app.route("/")
def main():
    return ("<h1>Guess a number between 0 and 9</h1>"
            "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>")


random_number = random.randint(0, 9)


@app.route("/<num>")
def num_check(num):
    if int(num) < random_number:
        return ("<h1>Too Low, try again!</h1>")
    elif int(num) > random_number:
        return ("<h1>Too high, try again!</h1>")
    elif int(num) == random_number:
        return ("<h1>Correct</h1>")

print(random_number)
if "__main__" == __name__:
    app.run(debug=True)
