from flask import Flask, render_template, request

app = Flask(__name__)


def sum_of_score(score1, score2, score3, score4, score5):
    return float(score1) + float(score2) + float(score3) + float(score4) + float(score5)


def is_all_checked(score1, score2, score3, score4, score5):
    return score1 and score2 and score3 and score4 and score5


def risk_category(total_score):
    if total_score <= 1.5:
        return "Very Low"
    elif 1.5 < total_score <= 3:
        return "Low"
    elif 3 < total_score <= 4.5:
        return "Intermediate"
    elif 4.5 < total_score <= 6:
        return "High"
    else:
        return "Very High"


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        score1 = request.form.get('my_radio1')
        score2 = request.form.get('my_radio2')
        score3 = request.form.get('my_radio3')
        score4 = request.form.get('my_radio4')
        score5 = request.form.get('my_radio5')
        if is_all_checked(score1, score2, score3, score4, score5):
            total_score = sum_of_score(score1, score2, score3, score4, score5)
            category = risk_category(total_score)
            return render_template('result.html', total_score=total_score, risk_category=category)
    return render_template('index.html')


if __name__ == "__main__":
    app.run()
