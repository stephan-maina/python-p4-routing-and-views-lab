#!/usr/bin/env python3
from flask import Flask, request

app = Flask(__name__)

# Component 1: Routing
@app.route('/')
def index():
    # Component 3: Response Handling
    return '<h1>Python Operations with Flask Routing and Views</h1>'

# Component 1: Routing
@app.route('/print/<string:string>')
def print_string(string):
    # Component 2: Request Handling
    # Manipulate and test the structure of a request object
    # Accessing query parameters from the request object
    query_param_value = request.args.get('param_name', 'default_value')

    # Component 3: Response Handling
    # Print the string to the console
    print(string)
    
    # Additional details about Cristiano Ronaldo
    additional_details = "Cristiano Ronaldo, commonly considered one of the greatest footballers of all time, has had a remarkable career spanning several top clubs, including Manchester United, Real Madrid, and Juventus. Known for his incredible speed, skill, and goal-scoring ability, Ronaldo has won numerous awards, including multiple Ballon d'Or titles."
    
    # Display the string in the web browser along with additional details about Cristiano Ronaldo
    return f'String: {string}, Query Parameter: {query_param_value}<br><br>{additional_details}'

# Component 1: Routing
@app.route('/count/<int:num>')
def count(num):
    # Component 3: Response Handling
    # Create a string with numbers in the specified range
    numbers = '\n'.join(str(i) for i in range(num))
    # Display the numbers in the web browser
    return numbers

# Component 1: Routing
@app.route('/math/<float:num1><operation><float:num2>')
def math(num1, operation, num2):
    result = None

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
        else:
            return 'Division by zero is not allowed.'
    elif operation == '%':
        result = num1 % num2

    if result is not None:
        return str(result)
    else:
        return 'Invalid operation.'

if __name__ == '__main__':
    # Component 7: Running the Development Server
    app.run(debug=True)
