from flask import Flask,request, send_from_directory

app = Flask(__name__)




@app.route('/')
def index():
    return send_from_directory("static",'index.html')


@app.route('/<path:path>')
def getsite(path):
    return send_from_directory('static', path)


if __name__ == '__main__':
    app.run()
