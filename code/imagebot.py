from flask import Flask, jsonify, request
from flask import render_template  # render html file
from classifier import classifier
from flask_bootstrap import Bootstrap
import numpy as np
import cv2
import io
from rcnn import object_detector
from nltk.corpus import wordnet as wn
from rcnn import core

app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/train')
def train():
    return render_template('train.html')


@app.route('/query')
def dealing_query():
    a = request.args.get('a', 0)
    result = classifier.get_result(a)
    intention = result.get('intention')
    parameter = result.get('parameter').get('target')
    if parameter is not None:
        parameter = wn.morphy(parameter)
    response = object_detector.switch_intention(intention, parameter)
    return jsonify(intention=str(intention), parameter=str(parameter), query=a, response=str(response))


@app.route('/upload', methods=['GET', 'POST'])
def dealing_image():
    if request.method == 'POST' and 'imagefile' in request.files:
        imagefile = request.files['imagefile']
        in_memory_file = io.BytesIO()
        imagefile.save(in_memory_file)
        data = np.fromstring(in_memory_file.getvalue(), dtype=np.uint8)
        color_image_flag = 1
        img = cv2.imdecode(data, color_image_flag)
        core.save_image(img)
    return 'success'


if __name__ == '__main__':
    app.run()
