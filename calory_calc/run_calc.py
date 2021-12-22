from re import L
from flask import Flask, render_template, request, flash

app=Flask(__name__)
app.config['SECRET_KEY']='ebdc451ec58fec34cb97f207'
@app.route('/', methods=['GET', 'POST'])
def index_page():
    if request.method == "POST":
        try:             
            calc_sex=request.form['calc_sex']
            calc_goal=request.form['calc_goal']             
            age=int(request.form['age'])            
            height=int(request.form['height'])            
            weight=float(request.form['weight'])
            life=float(request.form['life'])

            print('calc_sex = ', calc_sex)
            print("age = ", age)
            print('height = ', height)
            print('weight = ', weight)
            print('calc_goal = ', calc_goal) 
            print('life = ', life)

            ccal=0
            # расчёт для женщин на похудение
            if calc_sex == '2':
                if calc_goal == '1':
                    if weight >= 45 and weight < 50:
                        ccal = ((665 + 1.8 * height + 9.6 * weight * 0.985 - 4.7 * age) * life)*0.8
                    elif weight >= 50 and weight < 60:
                        ccal = ((665 + 1.8 * height + 9.6 * weight * 0.95 - 4.7 * age) * life)*0.8
                    elif weight >= 60 and weight < 80:
                        ccal = ((665 + 1.8 * height + 9.6 * weight * 0.9 - 4.7 * age) * life)*0.8
                    elif weight >= 80 and weight < 100:
                        ccal = ((665 + 1.8 * height + 9.6 * weight * 0.85 - 4.7 * age) * life)*0.8
                    elif weight >= 100:
                        ccal = ((665 + 1.8 * height + 9.6 * weight * 0.80 - 4.7 * age) * life)*0.8

                elif calc_goal == '2':
                    ccal = ((665 + 1.8 * height + 9.6 * (weight + 5) - 4.7 * age) * life)+300

                elif calc_goal == '3':
                        ccal = (665 + 1.8 * height + 9.6 * weight - 4.7 * age) * life
            # расчёты для мужчин
            elif calc_sex == '1':
                if calc_goal == '1':        
                    if weight >= 45 and weight < 50:
                            ccal = ((66 + 13.7 * weight * 0.985 + 5 * height - 6.8 * age) * life)*0.8
                    elif weight >= 50 and weight < 60:
                        ccal = ((66 + 13.7 * weight * 0.95 + 5 * height - 6.8 * age) * life)*0.8
                    elif weight >= 60 and weight < 80:
                        ccal = ((66 + 13.7 * weight * 0.9 + 5 * height - 6.8 * age) * life)*0.8
                    elif weight >= 80 and weight < 100:
                        ccal = ((66 + 13.7 * weight * 0.85 + 5 * height - 6.8 * age) * life)*0.8
                    elif weight >= 100:
                        ccal = ((66 + 13.7 * weight * 0.8 + 5 * height - 6.8 * age) * life)*0.8
                elif calc_goal == '2':
                    ccal = ((66 + 13.7 * (weight +5) + 5 * height - 6.8 * age) * life)+300
                elif calc_goal == '3':
                    ccal = ((66 + 13.7 * weight + 5 * height - 6.8 * age) * life)

            
            
            print('ccal = ', ccal)
            flash(f'рассчёт килокалорий составил {ccal}', category='info')
            return render_template('index.html', calc_sex=calc_sex, age=age, height=height, weight=weight, life=life)
        
        except:
            print('не все поля заполнены______')
            flash("заполните все поля", category='danger')
        

            

        

    if request.method == "GET":    
        return render_template('index.html')
    return render_template('index.html')

if __name__== ('__main__'):
    app.run(debug=True)
