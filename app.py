from flask import Flask,render_template,url_for,request
from instagram_bot_v3 import InstagramBot
app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/follow_explore',methods=['GET','POST'])
def follow_explore():
    uname = request.form['name']
    psw = request.form['pass']
    uname = str(uname)
    psw = str(psw)
    ig = InstagramBot(uname,psw)
    ig.login()
    ig.like_photo()
    ig.closeBrowser()
if __name__ == '__main__':
	app.run(port=8000,debug=True)
