from flask import Flask,render_template,request,redirect,url_for
import os
fileList = os.listdir('static/photo')
app = Flask(__name__)
@app.route('/',methods=['GET','POST'])
def home():
    global fileList
    if request.method=='POST':
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            print(uploaded_file.filename)
            uploaded_file.save('static/photo/'+uploaded_file.filename)
    fileList = os.listdir('static/photo')
    groupList=[]
    g1 = []
    for filename in fileList:
        g1.append('static/photo/'+filename)
        if len(g1)==4:
            groupList.append(g1)
            g1=[]
    if g1 not in groupList:
        groupList.append(g1)
    return render_template('01.html',groupList=groupList)
app.run('0.0.0.0',5000)