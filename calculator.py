from logging import Logger
from tkinter.tix import COLUMN
from flask import Flask, render_template, request
from  flask_sqlalchemy import SQLAlchemy

Flask_App = Flask(__name__) # Creating our Flask Instance


@Flask_App.route('/', methods=['GET'])
def index():
    """ Displays the index page accessible at '/' """

    return render_template('index.html')

@Flask_App.route('/operation_result/', methods=['POST'])
def operation_result():
    """Route where we send calculator form input"""

    error = None
    result = None

    # request.form looks for:
    # html tags with matching "name= "
    first_input = request.form['Input1']  
    second_input = request.form['Input2']
    operation = request.form['operation']

    try:
        input1 = float(first_input)
        input2 = float(second_input)

        # On default, the operation on webpage is addition
        if operation == "+":
            result = input1 + input2

        elif operation == "-":
            result = input1 - input2

        elif operation == "/":
            result = input1 / input2 

        elif operation == "*":
            result = input1 * input2

        else:
            operation = "%"
            result = input1 % input2

        return render_template(
            'index.html',
            input1=input1,
            input2=input2,
            operation=operation,
            result=result,
            calculation_success=True
        )
        
    except ZeroDivisionError:
        return render_template(
            'index.html',
            input1=input1,
            input2=input2,
            operation=operation,
            result="Неверная операция!",
            calculation_success=False,
            error="Вы не можете делить на 0"
        )
        
    except ValueError:
        return render_template(
            'index.html',
            input1=first_input,
            input2=second_input,
            operation=operation,
            result="Неверная операция!",
            calculation_success=False,
            error="Невозможно выполнить числовые операции с введёными данными"
        )

if __name__ == '__main__':
    Flask_App.debug = True
    Flask_App.run()
