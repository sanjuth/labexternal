from flask import Flask,render_template,request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/result', methods=['POST', 'GET'])
def result():
    username=request.args.get("username")
    c_upper=False
    c_lower=False
    c_digit=False
    for i in username:
        if i.isupper():
            c_upper=True
        if i.islower():
            c_lower=True
        if i.isdigit():
            c_digit=True
    return render_template('res.html',username=username,c_upper=c_upper,c_lower=c_lower,c_digit=c_digit)

if __name__ == '__main__':
    app.run(debug=True)
