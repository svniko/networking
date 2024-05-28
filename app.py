from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello, Flask!</h1>"

@app.route("/home/")
def homw():
    return render_template('hello.html')


@app.route('/error/')
def err():
    1/0
    
@app.route("/hello/", methods=['GET'])
def greet():
    name=request.form.get('name')
    name = 'дорогий(га) ' + name
    return render_template('hello.html', name=name)

if __name__ == '__main__':
    app.run(debug=True, port=8100)