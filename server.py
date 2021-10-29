from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template("index.html", times = 6, width = 6)

@app.route("/<int:num>")
def newchecker(num):
    return render_template("index.html", times = num, width = 8, color1 = "purple", color2 = "pink")

@app.route("/<int:num>/<int:num2>/<string:color1>/<string:color2>")
def newchecker3(num, num2, color1, color2):
    return render_template("index.html", times = num, width = num2, color1 = color1, color2 = color2)

if __name__=="__main__":
    app.run(debug=True)