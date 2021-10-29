from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template("index.html")

@app.route("/play/<int:num>")
def play_page(num):
    return num * 

if __name__=="__main__":
    app.run(debug=True)