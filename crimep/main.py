from flask import Flask, render_template, request , session ,redirect

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index1.html")


@app.route("/AddFIR")
def addfir():
    return render_template("firform.html")


@app.route("/AdminLogin")
def adminlogin():
    return render_template("adlogin.html")


@app.route("/Policedash")
def policelogin():
    return render_template("policedash.html")








if __name__ == "__main__":
    app.run(debug=True)      
