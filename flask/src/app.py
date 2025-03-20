from flask import Flask
import os
from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)
DEPLOYMENT=os.environ.get('DEPLOYMENT')

@app.route('/')
def index():
    return "<h1>Hello world!iashdfkjah</h1>"


if __name__ == '__main__':
    if DEPLOYMENT=='dev':
        app.run(host='0.0.0.0', port=6969, debug=True)
    elif DEPLOYMENT=='production':
        from waitress import serve
        serve(app, host="0.0.0.0", port=6969)
    else:
        print("Error")