from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    name = "Sarita"
    return render_template('exercise3.html',my_name=name)

if __name__ == "__main__":
    app.run(debug=True)
