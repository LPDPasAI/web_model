'''
 05/09/19
 
@author Leandro Paolo De Persiis
'''

from flask import Flask, render_template, request

app = Flask('web_model')

@app.route('/')
def show_predict_stock_form():
    return render_template('predictorform.html')


