from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


@app.route("/")
def home_page():
    return render_template("index.html")


@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open("database.txt", "a") as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        database.write(f"\n{email}, {subject}, {message}")


def write_to_csv_file(data):
    with open("database.csv", "a", newline="") as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(
            database, delimiter=",", quoting=csv.QUOTE_MINIMAL
        )
        csv_writer.writerow([email, subject, message])


@app.route("/submit-form", methods=["GET", "POST"])
def submit_form():
    write_to_csv_file(request.form.to_dict())
    return redirect("thankyou.html")


if __name__ == "__main__":
    app.run(debug=True)
