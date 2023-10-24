from flask import Flask, render_template, request, jsonify
import helper

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template('index.html')

@app.route("/math", methods = ["POST"])
def operations():
    if request.method == "POST":
        ops = request.form["operation"]
        try:
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])
        except Exception as e:
            result = "Please Enter integer or floating values!"
        else:
            if ops == "add":
                result = helper.add(num1, num2)
            if ops == "subtract":
                result = helper.substract(num1, num2)
            if ops == "multiply":
                result = helper.multiply(num1, num2)
            if ops == "divide":
                result = helper.division(num1, num2)
            if ops == "log":
                result = helper.log(num1, num2)
        return render_template("results.html", result = result)
        
@app.route("/postman_test", methods = ["POST"])
def postman_operations():
    if request.method == "POST":
        ops = request.json["operation"]
        try:
            num1 = float(request.json["num1"])
            num2 = float(request.json["num2"])
        except Exception as e:
            result = "Please Enter integer or floating values!"
        else:
            if ops == "add":
                result = helper.add(num1, num2)
            if ops == "subtract":
                result = helper.substract(num1, num2)
            if ops == "multiply":
                result = helper.multiply(num1, num2)
            if ops == "divide":
                result = helper.division(num1, num2)
            if ops == "log":
                result = helper.log(num1, num2)
        return jsonify(result)


if __name__=="__main__":
    app.run(host="0.0.0.0")
