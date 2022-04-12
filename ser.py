# import imp
from flask import Flask, g, render_template, request
from update_scrapeer import give_data
from mongodata import give_mongo_data,mycol
import html
import time

app = Flask(__name__)

@app.route('/')

def ind():
   give_data()
   return render_template('index.html')
   

@app.route('/gtu')
def gtu():
   give_data()
   return render_template('gtu_data.html')

@app.route('/add_mat')
def a_mat():
   return render_template('mat_manage.html')


@app.route('/data', methods=["GET", "POST"])
def data():
    data = {}
    if request.method == "POST":
        data['Name'] = request.form['subject']
        data['Material'] = request.form['material'] 
        data['url'] = request.form['url']
        mycol.insert_one(data)
    return render_template("mat_manage.html")


@app.route('/material')
def mat():
   mongo_data = give_mongo_data()
   return render_template("material.html",mat_data = mongo_data)

# @app.route('/result',methods = ['POST', 'GET'])
# def result():
#    if request.method == 'POST':
#       result = request.form
#       return render_template("result.html",result = result)



app.run(debug = True)