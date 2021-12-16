from flask import Flask, render_template
from controllers.index_controller import IndexController
from controllers.calculator_controller import CalculatorController
from controllers.history_controller import historyController

app = Flask(__name__)
app.secret_key = 'asrtarstaursdlarsn'

@app.route("/", methods=['GET'])
def index_get():
    return IndexController.get()

@app.route('/table/')
def table_get():
    return historyController.send()
@app.route('/testing/')
def testing():
    return render_template("testing.html")
@app.route('/tips/')
def tips():
    return render_template("tips.html")
@app.route('/code/')
def code():
    return render_template("ShowCode.html")
@app.route('/article/')
def article():
    return render_template("article4.html")



@app.route("/calculate/", methods=['GET'])
def calculator_get():
    return CalculatorController.get()

@app.route("/calculate/", methods=['POST'])
def calculator_post():
    return CalculatorController.post()

if __name__ == '__main__':
   app.run()

