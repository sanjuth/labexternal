from flask import Flask,request,render_template
app=Flask(__name__)

@app.route('/')
def homePage():
    return render_template('home.html')

@app.route('/welcome')
def welcome():
    uname=request.args.get("username")
    return f"hello {uname}"


if __name__=='__main__':
    app.run(debug=True)
