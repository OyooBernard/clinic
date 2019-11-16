from flask import Flask,render_template,url_for,request,redirect,session
app=Flask(__name__)
app.secret_key = 'super secret key'


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/user')
def user():
    return render_template('user.html')


@app.route('/logout')
def logout():
    session.pop('user',None)
    return redirect(url_for('login'))


@app.route('/login',methods=['GET','POST'])
def login():
     if request.method == 'POST':
         user=request.form['email']
         password=request.form['password']
         session['user']=request.form
         #session.commit()
         return redirect(url_for('user'))
     else:
        return render_template('login.html')



if(__name__)=='__main__':
    app.run(debug=True)
