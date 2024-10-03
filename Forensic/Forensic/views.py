"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, request
from Forensic import app

@app.route('/', methods=["GET", "POST"])
@app.route('/FS_WEBSITE')
def home():
    """Renders the home page."""
    return render_template(
        'FS_WEBSITE.html',
        title='Home Page',
        year=datetime.now().year,
    )
@app.route('/assign_value', methods=["POST"])
def assign_value():
    vertebra= [checkUnknown(request.form['c2']), checkUnknown(request.form['c3']), checkUnknown(request.form['c4']),
               checkUnknown(request.form['c5']), checkUnknown(request.form['c6']), checkUnknown(request.form['c7']),
               checkUnknown(request.form['t1']), checkUnknown(request.form['t2']), checkUnknown(request.form['t3']), 
               checkUnknown(request.form['t4']), checkUnknown(request.form['t5']), checkUnknown(request.form['t6']), 
               checkUnknown(request.form['t7']), checkUnknown(request.form['t8']), checkUnknown(request.form['t9']), 
               checkUnknown(request.form['t10']), checkUnknown(request.form['t11']),checkUnknown(request.form['t12']),
               checkUnknown(request.form['l1']), checkUnknown(request.form['l2']), checkUnknown(request.form['l3']),
               checkUnknown(request.form['l4']), checkUnknown(request.form['l5']) ]
    return render_template('FS_WEBSITE.html', results=vertebra)

def checkUnknown(x):
    if(x==''):
        return 0
    else:
        return float(x)

