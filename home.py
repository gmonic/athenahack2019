# import libraries
from flask import Flask, render_template, request
import requests
import json
import pandas
import 

# setup app
app = Flask("MyApp")

@app.route("/", methods=['GET','POST'])
def homepage():
    return render_template("index.html")


app.run(debug=True)