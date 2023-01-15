from flask import Flask, render_template, redirect, url_for,request

app = Flask(__name__)
app.config["SECRET_KEY"] = "xxxxxxxxxxx"


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/payment",methods=["GET","POST"])
def payment():
    if request.method == "POST":
        # email = request.form.get("email")
        return render_template("payment.html",state="done")
    return render_template("payment.html",state="confirm payment")

if __name__ == "__main__":
    app.run(debug=True)
