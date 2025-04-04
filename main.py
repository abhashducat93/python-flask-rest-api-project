from flask import Flask

app = Flask(__name__)

@app.route('/')  # This defines the root route
def home():
    return "Welcome to the Flask API!"

@app.route('/api')  # Another example route
def api():
    return {"message": "API response"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9001, debug=True)
