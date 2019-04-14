from flask import Flask, render_template, request

app = Flask("MyApp") 

@app.route('/')
def form():
    return render_template('main.html')

@app.route('/bronze.html')
def bronze():
    return render_template('bronze.html')

@app.route('/silver.html')
def silver():
    return render_template('silver.html')

@app.route('/gold.html')
def gold():
    return render_template('gold.html')

@app.route('/platinum.html')
def platinum():
    return render_template('platinum.html')

#this just adds point if recycled is true 

@app.route('/your_flask_funtion')
def get_ses():

     return render_template('upgrade.html') 


            #claim platinum prize button'''

app.run(debug=True)