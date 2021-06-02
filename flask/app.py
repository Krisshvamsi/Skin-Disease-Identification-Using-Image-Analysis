# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 19:48:45 2020

@author: Rahul
"""
import numpy as np
from flask import Flask,request,render_template
import os
from werkzeug.utils import secure_filename
app = Flask(__name__)
from keras.models import load_model
from keras.preprocessing import image
import tensorflow as tf
global graph
graph = tf.get_default_graph()
model = load_model("bmi_cnn.h5")
@app.route('/',methods = ["GET"] )
def index():
    return render_template("base.html")
@app.route('/predict',methods = ["GET","POST"])
def upload():
    if request.method == "POST":
        f = request.files["image"]
        basepath = os.path.dirname(__file__)
        print("current path: ",basepath)
        file_path = os.path.join(basepath,"uploads",secure_filename(f.filename))
        f.save(file_path)
        print("joined path: ",file_path)
        img = image.load_img(file_path,target_size = (64,64))
        x = image.img_to_array(img)
        x = np.expand_dims(x,axis = 0)
        with graph.as_default():
            p = model.predict_classes(x)
            print(p)
        index = ["cold sores","eczema","hives","melanoma","psoriasis"]
        text = "the predicted disease is : " +index[p[0]]
    return text
if __name__ == "__main__":
    app.run(debug = True)

