from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/",methods=['GET', 'POST'])
def calculator ():
    result = None
    if request.method == 'POST':
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operator = request.form['operation']

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            result = num1 / num2
    return render_template("index.html", result = result)