from flask import Flask, request, jsonify, render_template
from flask_cors import CORS, cross_origin
import requests

from datetime import datetime





app = Flask(__name__,static_url_path='', 
            static_folder='web/static',
            template_folder='templates')

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/getpage', methods=['GET', 'POST'])
@cross_origin()
def root():
    return "Hello from flask"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80,debug=True)
