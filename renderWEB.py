from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from werkzeug.utils import secure_filename
import creatDIR
import craft
import os
import URLaddress



app = Flask(__name__)
bootstrap = Bootstrap(app)

RAINBOW_COLORS = ['red', 'orange', 'yellow', 'green', 'cyan', 'blue', 'violet']
@app.route("/")
@app.route("/Home Page", methods=["GET"])
def home_page():
    return render_template("HomePage.html", title="Home Page")


@app.route("/Creating QR-code", methods=["GET", "POST"])
def creating():
    print(request.form.get("link"))
    return render_template("creatingQR-code.html")

@app.route("/submit", methods=["GET", "POST"])
def submit():
    link = request.form.get("user_input")
    inf_about_QR = craft.creating_QR_code(link, "w")
    return render_template("creatingQR-code.html", trip_img=inf_about_QR[0], status_gen=inf_about_QR[1],  colors=RAINBOW_COLORS)


@app.errorhandler(404)
def error404(error):
    return render_template("page404.html", error=error)





@app.route("/upload", methods=["GET", "POST"])
def upload():

    UPLOAD_FOLDER = "static/imagesQR/images_open"
    app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

    if request.method == "POST":
        file = request.files["image"]

        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        file.save(file_path)
        link, status = craft.recognize_qr_code_and_print_link(f"static/imagesQR/images_open/{filename}")


        print(link, status)

    return render_template("recognizeQR-code.html", link=link)




if __name__ == "__main__":

    creatDIR.creat_DIR_site()

    app.run(debug=True, port=80000, host='0.0.0.0')

    creatDIR.delit_DIR_site()