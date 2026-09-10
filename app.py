from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    selected_date = None

    if request.method == "POST":
        selected_date = request.form.get("date")

    return render_template(
        "index.html",
        selected_date=selected_date
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)