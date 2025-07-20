from flask import Flask, render_template, request, send_file, send_from_directory
import numpy as np

import os
import cv2

import requests
import json
import keras
import numpy as np
import scipy.io as sio
import scipy.stats as sst

import load
import network
import util







app = Flask(__name__, static_folder='static', template_folder='templates')


def predictecg(record):
    ecg = load.load_ecg(record)
    preproc = util.load(".")
    x = preproc.process_x([ecg])

    params = json.load(open("config.json"))
    params.update({
        "compile" : False,
        "input_shape": [None, 1],
        "num_categories": len(preproc.classes)
    })

    model = network.build_network(**params)
    model.load_weights('model.hdf5')

    probs = model.predict(x)
    prediction = sst.mode(np.argmax(probs, axis=2).squeeze())[0][0]
    return preproc.int_to_class[prediction]




@app.route('/')
def home():
    return render_template("index.html")



@app.route('/predict', methods=['POST', 'GET'])
def predict():
    if request.method == 'POST':
        # try:
            img = request.files['webcam']
            img.save("matfile.mat")
            print(img)
            # npmat = np.frombuffer(img, dtype=np.int16)
            a = predictecg("matfile.mat")
            print(a)
            filename = "No file Name"
            response  = "Signal is Noramal"
            perc = 100
            return render_template("index.html", img_src=filename, predict=a, percent=str(perc) + " %")
        # except:
        #     return render_template("index.html")


    if request.method == 'GET':
        return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True, threaded=False)