from flask import Flask, request, render_template

# check a commit

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        number1 = request.form.get('number1', type=float)
        number2 = request.form.get('number2', type=float)
        operation = request.form.get('operation')

        if operation == 'add':
            result = number1 + number2
        elif operation == 'subtract':
            result = number1 - number2
        elif operation == 'multiple':
            result = number1 * number2
        elif operation == 'devide':
            try:
                result = number1 / number2
            except ZeroDivisionError as e:
                result = 'Wrong caclutation. Zero devided.'
        return render_template('template_first.html', result=result)
    else:
        return render_template('template_first.html', result=None)

if __name__ == '__main__':
    app.run(debug=True)
