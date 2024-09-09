from flask import Flask, render_template
import creatDIR

app = Flask(__name__)


@app.route("/")
@app.route("/Home Page")
def home_page():
    return render_template("HomePage.html", title="Home Page")


@app.route("/Creating QR-code")
def creating():
    return render_template("creatingQR-code.html")


@app.route("/Recognize QR-code")
def recognize():
    return render_template("recognizeQR-code.html")


@app.errorhandler(404)
def erroe404(error):
    return render_template('page404.html', error=error)


if __name__ == "__main__":
    creatDIR.creat_DIR()
    app.run(debug=True)
    creatDIR.delit_DIR()
