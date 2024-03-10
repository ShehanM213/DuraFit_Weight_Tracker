from flask.app import Flask
from flask import Flask
app = Flask(__name__)
from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
