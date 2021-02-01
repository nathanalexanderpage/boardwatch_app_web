from flask import Flask, render_template

app = Flask(__name__)

nav = [
    {
        'name': 'account',
        'url': '#'
    },
    {
        'name': 'search',
        'url': '#'
    },
    {
        'name': 'catalog',
        'url': '#'
    },
    {
        'name': 'info',
        'url': '#'
    }
]

@app.route('/')
def index():
    return render_template('index.html', nav=nav)
