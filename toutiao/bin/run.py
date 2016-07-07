#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('UTF8')
sys.path.append('..')
from flask import Flask
from flask import send_from_directory, request, Response
from flask import render_template
import random
from data import res_dict




app = Flask(__name__, static_folder="../static", template_folder="../templates")


@app.route('/<path:filename>')
def send_file(filename):
    return send_from_directory(app.static_folder, filename)

@app.route('/')
def index():
    return render_template('index.tmpl',
                           res_dict=res_dict)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
