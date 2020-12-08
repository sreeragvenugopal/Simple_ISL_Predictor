import numpy as np
from flask import Flask, render_template, request
import pickle
import pandas as pd

filename = 'islscore.pkl'
regressor = pickle.load(open(filename, 'rb'))

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/predict', methods=['POST'])
def predict():
    f_array = list()
    o_array = list()
    play = list()

    if request.method == 'POST':

        focusteam = request.form['Focus-team']
        if focusteam == 'NorthEast United FC':
            f_array = f_array + [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
        elif focusteam == 'FC Goa':
            f_array = f_array + [0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
        elif focusteam == 'Jamshedpur FC':
            f_array = f_array + [0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
        elif focusteam == 'ATK':
            f_array = f_array + [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        elif focusteam == 'Chennaiyin FC':
            f_array = f_array + [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
        elif focusteam == 'Kerala Blasters FC':
            f_array = f_array + [0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
        elif focusteam == 'Mumbai City FC':
            f_array = f_array + [0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
        elif focusteam == 'Bengaluru FC':
            f_array = f_array + [0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
        elif focusteam == 'Odisha FC':
            f_array = f_array + [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
        elif focusteam == 'Hyderabad FC':
            f_array = f_array + [0, 0, 0, 0, 1, 0, 0, 0, 0, 0]

        opponentteam = request.form['Opponent-team']
        if opponentteam == 'NorthEast United FC':
            o_array = o_array + [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
        elif opponentteam == 'FC Goa':
            o_array = o_array + [0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
        elif opponentteam == 'Jamshedpur FC':
            o_array = o_array + [0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
        elif opponentteam == 'ATK':
            o_array = o_array + [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        elif opponentteam == 'Chennaiyin FC':
            o_array = o_array + [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
        elif opponentteam == 'Kerala Blasters FC':
            o_array = o_array + [0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
        elif opponentteam == 'Mumbai City FC':
            o_array = o_array + [0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
        elif opponentteam == 'Bengaluru FC':
            o_array = o_array + [0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
        elif opponentteam == 'Odisha FC':
            o_array = o_array + [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
        elif opponentteam == 'Hyderabad FC':
            o_array = o_array + [0, 0, 0, 0, 1, 0, 0, 0, 0, 0]

        fscore = int(request.form['F_score'])
        systemplay = request.form['play']
        if systemplay == '3-4-1-2':
            play = play + [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        elif systemplay == '3-4-2-1':
            play = play + [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        elif systemplay == '3-4-3':
            play = play + [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        elif systemplay == '3-5-2':
            play = play + [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
        elif systemplay == '4-1-4-1':
            play = play + [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
        elif systemplay == '4-2-3-1':
            play = play + [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
        elif systemplay == '4-3-1-2':
            play = play + [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
        elif systemplay == '4-3-3 Attacking':
            play = play + [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
        elif systemplay == '4-4-1-1':
            play = play + [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
        elif systemplay == '4-4-2 double 6':
            play = play + [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
        elif systemplay == '4-5-1':
            play = play + [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
        elif systemplay == '5-3-2':
            play = play + [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]

        temp_array = [fscore] + o_array + f_array + play

        data = np.array([temp_array])
        my_prediction = int(regressor.predict(data))
        if my_prediction == 0:
            return render_template('result.html', result="DRAW")
        elif my_prediction == 2:
            return render_template('result.html', result="WIN")
        elif my_prediction == 1:
            return render_template('result.html', result="LOSS")


if __name__ == '__main__':
    app.run(debug=True)
