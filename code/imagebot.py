import io
import cv2
import numpy as np
from flask import Flask, jsonify, request
from flask import render_template
from flask_bootstrap import Bootstrap
from classifier import query_parser, intention_chooser
from core import rcnn

app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/train')
def train():
    return render_template('train.html')


@app.route('/query', methods=['GET', 'POST'])
def dealing_query():
    a = request.args.get('a', 0)
    intention, parameter = query_parser.parse_query(a)
    response = intention_chooser.switch_intention(intention, parameter)
    return jsonify(intention=str(intention), parameter=str(parameter), query=a, response=str(response))


@app.route('/upload', methods=['GET', 'POST'])
def dealing_image():
    try:
        if request.method == 'POST' and 'imagefile' in request.files:
            imagefile = request.files['imagefile']
            in_memory_file = io.BytesIO()
            imagefile.save(in_memory_file)
            data = np.fromstring(in_memory_file.getvalue(), dtype=np.uint8)
            img = cv2.imdecode(data, 1)
            rcnn.save_image(img)
        return jsonify(status='success')
    except:
        return jsonify(status='error')


if __name__ == '__main__':
    app.run()
