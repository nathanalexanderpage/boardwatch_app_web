from flask import Flask, render_template
import requests

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

@app.route('/platforms/<platform_id>')
def platform_by_id(platform_id):
    r = requests.get(f"http://127.0.0.1:5001/platforms/{platform_id}")

    return render_template('platforms-one.html', nav=nav, platform=r.json())
