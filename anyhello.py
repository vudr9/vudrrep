from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p style='color: blue; font-size: 50px;'>Hello, World!</p>"

if __name__ == '__main__':
    app.run()







