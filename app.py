from flask import Flask, render_template, request
from logic import add, multiply, divide, subtract

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        # Get user input from the form
        number1 = float(request.form['number1'])
        number2 = float(request.form['number2'])
        operation = request.form['operation']

        # Perform the calculation
        if operation == 'add':
            result = add(number1,number2)
        elif operation == 'subtract':
            result = subtract(number1,number2)
        elif operation == 'multiply':
            result = multiply(number1,number2)
        elif operation == 'divide':
            result = divide(number1,number2)
        else:
            result = 'Invalid operation'

        return render_template('index.html', result=result)
    except Exception as e:
        return render_template('index.html', result=str(e))

if __name__ == '__main__':
    app.run(debug=True)
