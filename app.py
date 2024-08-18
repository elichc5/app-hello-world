from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Francisco bienvenido a tu App hecha con Python'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)