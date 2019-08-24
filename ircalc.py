from flask import Flask, request, render_template, url_for

# Creates the application for the flask
app = Flask(__name__)

# Uses a decorator to display the index page
@app.route('/')
def index():
    return render_template('index.html')

# Uses a decorator to link the function
@app.route('/interest', methods=['GET', 'POST'])

# Defines interest Calculation Function
def interest():
    if request.method =='POST':
# Pulls balance and monthly payment from form
        balance = int(request.form.get('balance'))
        monthlyPayment = int(request.form.get('monthlyPayment'))

# Calculates the interest payment by subtraction 1% of the balance from the monthly payment.
        interestPayment = monthlyPayment - (balance * .01)
        principalPayment = balance * .01
# Calculates the interest rate by checking that the Interest Rate that is ranging divided by 100 for 100 percent, then divided by 12 months in a year multiplied by the balance is equal to the interest payment
        for interestRate in range(0, 30):
            interestRate += 1
            if (((int(interestRate) / 100) / 12) * balance) == interestPayment:
                interestRate -= .01
                return render_template('calc.html', interestPayment=interestPayment, principalPayment=principalPayment, interestRate=interestRate)
        
# Starts Flask Server
app.run()
