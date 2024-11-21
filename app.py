from flask import Flask

# Create Flask application
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, welcome to my web app deployed on GCP!"

# Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
