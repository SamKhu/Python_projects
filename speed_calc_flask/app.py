# python programm using flask for speed calculator


from flask import Flask, render_template, request

app=Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index_page():
    if request.method=='POST':
        distance=float(request.form['distance'])
        time=float(request.form['time'])
        speed=round((distance/time), 3)
        return render_template('calc_speed.html', distance=distance, time=time, speed=speed)

    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)

