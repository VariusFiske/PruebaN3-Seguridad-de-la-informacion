from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    password = input("Enter password: ")  # inseguro, detectado por Bandit
    assert password != "1234"  # inseguro
    return "Hello, Security!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
