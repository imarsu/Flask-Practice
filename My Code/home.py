from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/form',methods=['GET','POST'])
def form_response():
    if request.method=='POST':
        first = request.form.get('first')
        last = request.form.get('last')
    return render_template('form_response.html',first=first, last=last)


if __name__=='__main__':
    app.run(debug=True)