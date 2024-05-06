from flask import Flask  # Import the Flask module

app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True)
