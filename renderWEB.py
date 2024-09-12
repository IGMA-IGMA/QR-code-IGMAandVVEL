from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import creatDIR
import craft
import os


app = Flask(__name__)


@app.route("/")
@app.route("/Home Page", methods=["GET"])
def home_page():
    return render_template("HomePage.html", title="Home Page")


@app.route("/Creating QR-code", methods=["GET", "POST"])
def creating():
    print(request.form.get('link'))
    return render_template("creatingQR-code.html")


@app.route("/Recognize QR-code", methods=["GET", "POST"])
def recognize():
    return render_template("recognizeQR-code.html", title="Recognize QR-codeсщв")


@app.errorhandler(404)
def error404(error):
    return render_template('page404.html', error=error)


@app.route('/submit', methods=["GET", "POST"])
def submit():
    link = request.form.get('user_input')
    inf_about_QR = craft.creating_QR_code(link)
    return render_template("creatingQR-code.html", trip_img=inf_about_QR[0], status_gen=inf_about_QR[1])

@app.route('/upload', methods=["GET", "POST"])
def upload():

    UPLOAD_FOLDER = 'static/imagesQR/images_open'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    if request.method == "POST":
        file = request.files["image"]

        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        #print(f"static/imagesQR/images_open/{filename}")
        link, status = craft.recognize_qr_code_and_print_link(f"static/imagesQR/images_open/{filename}")
        print(link)

    return render_template("upload.html", link=link)




if __name__ == "__main__":

    creatDIR.creat_DIR()

    app.run(debug=True, port=1000)

    creatDIR.delit_DIR()