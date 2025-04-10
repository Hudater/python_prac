from flask import Flask
import os
from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)
DEPLOYMENT=os.environ.get('DEPLOYMENT')
HOST=os.environ.get('HOST')
PORT=os.environ.get('PORT')


@app.route('/')
def index():
    return "<h1>Hello world!iashdfkjah</h1>"


if __name__ == '__main__':
    if DEPLOYMENT=='dev':
        app.run(host=HOST, port=PORT, debug=True)
    elif DEPLOYMENT=='prod':
        from waitress import serve
        serve(app, host=HOST, port=PORT)
    else:
        print("Error")
