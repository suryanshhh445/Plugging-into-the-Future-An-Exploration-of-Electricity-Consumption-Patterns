from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # This will render the index.html file from the 'templates' folder
    return render_template('index.html')

if __name__ == '__main__':
    # The debug=True flag allows for automatic reloading when you save changes
    app.run(debug=True)
