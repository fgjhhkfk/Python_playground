from flask import Flask, render_template, request
from forms import ButtonForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '1243124312431243'


@app.route('/', methods=['GET', 'POST'])
def hello_world():

    if request.method == 'POST':
        print("erstes if")
        if request.form['button'] == 'submit':
            print("zweites if")
            value = 1
    elif request.method == 'GET':
        print("elif")
        value = 0

    return render_template("button.html", value=value)


if __name__ == '__main__':
    app.run(debug=True)
