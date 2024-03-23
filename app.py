from flask import Flask, render_template, redirect, url_for
from forms import Questionnaire
app = Flask(__name__)
app.secret_key = "Yesulensecret"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/information")
def information():
    return render_template("information.html")


@app.route("/questionnaire", methods=['GET', 'Post'])
def questionnaire():
    form = Questionnaire()
    if form.validate_on_submit():
        with open('submissions.txt', 'a') as file:
            file.write(f"Name: {form.name.data}\n")
            file.write(f"Course: {form.course.data}\n")
            file.write(f"Short-form Answer: {form.short_answer.data}\n")
            file.write(f"Long-form Answer: {form.long_answer.data}\n")
            file.write(f"Overall Satisfaction: {form.satisfaction.data}\n")
            file.write(f"Would recommend: {form.recommend.data}\n")
            file.write(f"Suggestions for Improvement: {form.improvements.data}\n")
            file.write('\n')
        return redirect(url_for('submitted'))
    return render_template('questionnaire.html', form=form)


@app.route('/submitted')
def submitted():
    return 'Your form has been submitted successfully.'


if __name__ == '__main__':
    app.run(debug=True)