import os
from flask import Flask, request, render_template
historys=""
app = Flask(__name__)
@app.route('/')
def index():
    path=os.popen('pwd').read()
    return render_template('index.html', cwdp=path)
@app.route('/run', methods=['POST'])
def send():
    global historys
    command = request.form['command']
    if 'cd ' in command:
        comlis=command.split('cd ')
        try:
            comlis[1]=comlis[1].replace('~', '/home/aaa')
        except:
            pass
        try:
            os.chdir(comlis[1])
        except:
            pass
    var=os.popen(command).read()
    historys=command+'\n'+var+'\n'+historys+'\n'
    finalcom = historys.replace('\n', '<br>')
    path=os.popen('pwd').read()
    return render_template('index.html', command=finalcom, cwdp=path)