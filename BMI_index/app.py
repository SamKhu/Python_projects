from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def calculate():
    bmi = ''
    if request.method=='POST' and 'вес' in request.form and 'рост' in request.form:
        print('*'*60)
        Weight=float(request.form.get('вес'))
        Height=float(request.form.get('рост'))
        bmi=(round(Weight/(Height/100)**2),2)

    return render_template("index.html", bmi=bmi)

