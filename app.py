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

@app.route("/questionnaire", methods=['GET', 'POST'])
def questionnaire():
    form = Questionnaire()
    if form.validate_on_submit():
        # Debugging message to check if form validation is successful
        print("Form validation successful")

        with open('submissions.txt', 'a') as file:
            file.write(f"Name: {form.first_name.data} {form.last_name.data}\n")
            file.write(f"Email: {form.email.data}\n")
            file.write(f"Student Number: {form.student_number.data}\n")
            file.write(f"Programme Type: {form.programme_type.data}\n")
            file.write(f"Grades: {form.grades.data}\n")
            file.write(f"Overall Satisfaction: {form.satisfaction.data}\n")
            if form.suggestions.data:
                file.write(f"Suggestions: {form.suggestions.data}\n")
                file.write('\n')

        # Debugging message to ensure the redirection is attempted
        print("Redirecting to submitted page")
        return redirect(url_for('submitted'))

    # Debugging message to check if form validation fails
    print("Form validation failed")
    return render_template('questionnaire.html', form=form)

@app.route('/submitted')
def submitted():
    return 'Your form has been submitted successfully.'

if __name__ == '__main__':
    app.run(debug=True)
