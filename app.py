"""
SOURCES:
#https://www.youtube.com/watch?v=Z1RJmh_OqeA&ab_channel=freeCodeCamp.org
#https://flask.palletsprojects.com/en/1.1.x/patterns/fileuploads/
#https://stackoverflow.com/questions/27539309/how-do-i-create-a-link-to-another-html-page
"""

from flask import Flask, render_template, flash, request, send_file
import os
from random import seed, randint
from make_route import collectTurnPoints
import webbrowser
from file_handler import *
#from pyfladesk import init_gui

from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/'
ALLOWED_EXTENSIONS = {'gpx'}
API_STUFFS = {'api_key':'Anbq6gN1whgpvjU28wqG9AH3iQPUXyXY'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

#set up route to base of app?
@app.route('/' , methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print(request.files)
        try:
            print("this is what we got:"+request.form['apikey']+":")
            if(request.form['apikey'].replace(" ", "") != ''):
                print("putting the key: ", request.form['apikey'], " into the dict")
                API_STUFFS['api_key'] = str(request.form['apikey'])
        except:
            print("using our api key instead")
            API_STUFFS['api_key'] = "Anbq6gN1whgpvjU28wqG9AH3iQPUXyXY"

        # check if post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            print("this")
        file = request.files['file']
        # if user does  not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('no selected file')
            print("that")
            return render_template('submiterror.html')
        if file and allowed_file(file.filename):
            #filename = secure_filename(file.filename)
            #file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            file.save('input/' + 'newRoute' + str(randint(0,9999)) + '.gpx')
            print("shit got put into " + UPLOAD_FOLDER)
            #return redirect(url_for('uploaded_file', filename=filename))
            return render_template('index.html')
        else:
            return render_template('submiterror.html')

    # show the form, it wasn't submitted
    return render_template('index.html')

@app.route('/convert_input/')
def convert_input():
    print("combine this shit so it'll actually do the fucking converting")
    collectTurnPoints(getNewestInput(), API_STUFFS['api_key'])
    #return render_template('index.html')

@app.route('/return_result/')
def return_result():
    print("gonna send the file back to this user biatch")
    if os.listdir('output') == []:
        print("error in creating output")
        #GET THIS THIS TO RENDER HTML ERROR PAGE FOR OUTPUT
    else:
        output = getNewestOuput()
        return send_file(getNewestOuput())
    return render_template('index.html')

def start():
    #app.secret_key = os.urandom(24)
    #app.config['SESSION_TYPE'] = 'filesystem'
    app.run(debug = True)
    #init_gui(app)

if (__name__ == "__main__"):
    webbrowser.open('http://localhost:5000')
    start()
