from flask import Flask, url_for

app = Flask(__name__)

@app.route("/")
def main():
    return '''<h1>Hello world!</h1>'''

if __name__ == '__main__':
    app.run(host='0.0.0.0')
