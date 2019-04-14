# import libraries
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import requests
import json
import pandas
import io
import os

# import the google cloud client library
from google.cloud import vision
from google.cloud.vision import types


# export GOOGLE_APPLICATION_CREDENTIALS="/Users/monicagupta/athenahack2019/athenahack2019-093aba2234d7.json"


# instantiate a client
client = vision.ImageAnnotatorClient()

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
UPLOAD_FOLDER = '/Users/monicagupta/athenahack2019/static/'


# setup app
app = Flask("MyApp")
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/", methods=['GET','POST'])
def homepage():
    if request.method == 'POST':      
 # check if the post request has the file part
        if 'file' not in request.files:
            print('hello1')
            return render_template("index.html")
        file = request.files['file']
        print('hello2')
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '': 
            return render_template("index.html")
            print('hello3')
        if file:
            print('hello4')
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            # f = request.files['file']
            # f.save(secure_filename(f.filename)) 
            print('file:')
            print(file)   
            path = "/Users/monicagupta/athenahack2019/static/" + file.filename
            file_name = file.filename
            with open(path, 'rb') as image_file:
                content = image_file.read()
            image = vision.types.Image(content=content)  
            
            objects = client.object_localization(
                image=image).localized_object_annotations
            for object_ in objects:
                print('Number of objects found: {}'.format(len(objects)))
                print('\n{} (confidence: {})'.format(object_.name, object_.score))
                print('Normalized bounding polygon vertices: ')
                for vertex in object_.bounding_poly.normalized_vertices:
                    print(' - ({}, {})'.format(vertex.x, vertex.y))

            object = objects[0]

            # content = file.read()
            # print('content:')
            # print(content)
            # image = vision.types.Image(content=content)
            # objects = client.object_localization(image=image).localized_object_annotations
            # print('Number of objects found: {}'.format(len(objects)))
            # for object_ in objects:
            #     print('\n{} (confidence: {})'.format(object_.name, object_.score))
            #     print('Normalized bounding polygon vertices: ')
            # for vertex in object_.bounding_poly.normalized_vertices:
            #     print(' - ({}, {})'.format(vertex.x, vertex.y))
            return render_template("index.html", object=object, file_name=file_name, path=path)
        
        return render_template("index.html")
    else:
        return render_template("index.html")


app.run(debug=True)