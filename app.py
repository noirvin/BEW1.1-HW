from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    """Renders the home page with link to Fortune page."""
    return render_template('index.html')
