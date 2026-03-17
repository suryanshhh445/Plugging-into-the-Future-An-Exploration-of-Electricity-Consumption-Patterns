"""
app.py
Entry point for the Flask web application.
Serves the index.html template containing the embedded Tableau visualisations.
"""
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
