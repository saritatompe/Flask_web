from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index2.html')

# @app.route("/signup_form")
# def signup_form():
#     return render_template('signup.html')


if __name__ == "__main__":
    app.run(debug=True)
