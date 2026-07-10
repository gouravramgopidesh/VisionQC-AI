from flask import Flask, render_template, request
import os
import webbrowser
from threading import Timer

from predict import predict_image
from database import (
    init_db,
    save_prediction,
    get_predictions,
    clear_history
)
from report_generator import generate_report
from flask import send_file
app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Create database
init_db()


@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        if "image" not in request.files:
            history = get_predictions()
            return render_template("index.html", history=history)

        file = request.files["image"]

        if file.filename == "":
            history = get_predictions()
            return render_template("index.html", history=history)

        filepath = os.path.join(
            app.config["UPLOAD_FOLDER"],
            file.filename
        )

        file.save(filepath)

        prediction, confidence = predict_image(filepath)

        report_path = generate_report(
        file.filename,
        prediction,
        confidence
)

        # Save prediction to database
        save_prediction(
            file.filename,
            prediction,
            confidence
        )

        history = get_predictions()

        return render_template(
    "index.html",
    image=file.filename,
    prediction=prediction,
    confidence=confidence,
    history=history,
    report_path=report_path
)

    history = get_predictions()

    return render_template(
        "index.html",
        history=history
    )
@app.route("/clear_history", methods=["POST"])
def clear():

    clear_history()

    return render_template(
        "index.html",
        history=[]
    )

@app.route("/download_report")
def download_report():

    reports_folder = "reports"

    reports = sorted(
        os.listdir(reports_folder),
        reverse=True
    )

    if not reports:
        return "No report found."

    latest_report = os.path.join(
        reports_folder,
        reports[0]
    )

    return send_file(
        latest_report,
        as_attachment=True
    )
def open_browser():
    webbrowser.open("http://127.0.0.1:5000")

if __name__ == "__main__":
    Timer(1, open_browser).start()
    app.run(debug=True)