from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # because folder name is templates you don't have to specify route
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)