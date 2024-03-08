import randomizer
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def render_html():
    number_to_guess = randomizer.randomize()
    return render_template('index.html', value = number_to_guess)

if __name__ == '__main__':
    app.run()

