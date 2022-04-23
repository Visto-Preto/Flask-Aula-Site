# coding: utf-8

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/tipoget')
def ir_get():
    return render_template('get.html')

@app.route('/tipopost')
def ir_post():
    return render_template('post.html')

@app.route('/userpage/', methods=['GET', 'POST'])
def userpage():
    if request.method == "GET":
        user = request.args.get("user")
        passw = request.args.get("passw")
        mt = "GET"

    elif request.method == "POST":
        user = request.args.get("user")
        passw = request.args.get("passw")
        mt = "POST"

    return render_template('userpage.html', user=user, passw=passw, mt=mt)

if __name__ == '__main__':
    app.run(debug=True)
